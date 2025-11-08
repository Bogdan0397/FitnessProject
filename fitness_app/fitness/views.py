from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.decorators import method_decorator

from .models import Programs, Exercises
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from fuzzywuzzy import fuzz
from .utils import FitnessMixin, apply_skyline_filter, parse_fuzzy_query



def home(request):

    return render(request,'fitness/home.html',)

def about(request):
    return render(request,'fitness/about.html',context={'selected_menu':'About'})

def contact(request):
    return render(request,'fitness/contact.html',context={'selected_menu':'About'})

def workouthome(request):
    return render(request, 'fitness/workout_home.html',context={'selected_menu':'Workout'})

class ProgramsHome(FitnessMixin,ListView):
    template_name = 'fitness/programs_home.html'
    context_object_name = 'programs'
    allow_empty = True

    def get_queryset(self):
        qs = Programs.objects.all()

        query = (self.request.GET.get('q') or '').strip().lower()
        difficulty = self.request.GET.get('difficulty') or ''
        duration = self.request.GET.get('duration') or ''
        goal = self.request.GET.get('goal') or ''

        used_filters = False

        # --- 1. Звичайний і нечіткий пошук ---
        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))
            used_filters = True

        if difficulty:
            qs = qs.filter(difficulty=difficulty)
            used_filters = True

        if duration:
            qs = qs.filter(duration=duration)
            used_filters = True

        if goal:
            qs = qs.filter(goal=goal)
            used_filters = True

        # --- 2. Визначення цілі за змістом запиту ---
        GOAL_SYNONYMS = {
            "weight_loss": ["weight", "fat", "loss", "burn", "slim"],
            "strength": ["strength", "muscle", "power", "gain", "bulk"],
            "endurance": ["endurance", "stamina", "cardio"],
            "mobility": ["mobility", "flexibility", "stretch", "yoga"]
        }

        detected_goal = None
        best_score = 0
        for goal_key, synonyms in GOAL_SYNONYMS.items():
            for word in synonyms:
                score = fuzz.token_set_ratio(query, word)
                if score > 70 and score > best_score:
                    best_score = score
                    detected_goal = goal_key

        # --- 3. М'яке фільтрування по цілі ---
        if detected_goal:
            qs_goal = Programs.objects.filter(goal=detected_goal)
            if qs.exists():
                qs = (qs | qs_goal).distinct()  # додаємо програми з виявленою ціллю
            else:
                qs = qs_goal
            used_filters = True

        # --- 4. Skyline (контекстний відбір) ---
        if used_filters:
            criteria = {"difficulty": "min", "duration": "min"}

            if detected_goal == "strength":
                criteria = {"difficulty": "max", "duration": "max"}
            elif detected_goal == "endurance":
                criteria = {"difficulty": "max", "duration": "max"}
            elif detected_goal == "mobility":
                criteria = {"difficulty": "min", "duration": "min"}
            elif detected_goal == "weight_loss":
                criteria = {"difficulty": "min", "duration": "min"}

            print("Detected goal:", detected_goal)
            print("Skyline criteria:", criteria)

            skyline = apply_skyline_filter(qs, criteria)
            qs = qs.filter(id__in=[p.id for p in skyline])

        # --- 5. fallback якщо нічого не знайдено ---
        if not qs.exists() and query:
            qs = Programs.objects.filter(
                Q(name__icontains="weight") | Q(description__icontains="weight")
            )

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        default_program_photo = settings.DEFAULT_PROGRAM_IMAGE

        context.update({
            'selected_difficulty': self.request.GET.get('difficulty', ''),
            'selected_duration':   self.request.GET.get('duration', ''),
            'selected_goal':       self.request.GET.get('goal', ''),
            'difficulty_choices':  Programs.DIFFICULTY_CHOICES,
            'duration_choices':    Programs.DURATION_CHOICES,
            'goal_choices':        Programs.GOAL_CHOICES,
        })

        return self.get_mixin_context(context, default_program_photo=default_program_photo)

class Program(FitnessMixin,DetailView):
    template_name = 'fitness/program.html'
    slug_url_kwarg = 'program_slug'
    context_object_name = 'program'
    def get_object(self):
        return get_object_or_404(Programs,slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        default_program_photo = settings.DEFAULT_PROGRAM_IMAGE
        return self.get_mixin_context(context, default_program_photo=default_program_photo)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        program = self.get_object()
        user = request.user

        # Просто назначаем выбранную фитнес-программу
        user.selected_fitness_program = program
        user.save()

        return redirect('user:profile')

class ExerciseView(FitnessMixin,DetailView):
    template_name = 'fitness/exercise_detail.html'
    slug_url_kwarg = 'exercise_slug'
    context_object_name = 'exercise'

    def get_object(self):
        return get_object_or_404(Exercises, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        default_exercise_image = settings.DEFAULT_EXRCISE_IMAGE
        return self.get_mixin_context(context, default_exercise_image=default_exercise_image)
