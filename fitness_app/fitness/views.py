from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.decorators import method_decorator

from fitness.models import Programs, Exercises
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from fitness.utils import FitnessMixin


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
        query = self.request.GET.get('q')
        difficulty = self.request.GET.get('difficulty')
        duration = self.request.GET.get('duration')
        goal = self.request.GET.get('goal')

        qs = Programs.objects.all()

        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if difficulty:
            qs = qs.filter(difficulty=difficulty)

        if duration:
            qs = qs.filter(duration=duration)

        if goal:
            qs = qs.filter(goal=goal)

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