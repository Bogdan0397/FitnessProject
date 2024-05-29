from django.shortcuts import render
from django.conf import settings
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
    allow_empty = False

    def get_queryset(self):
        return Programs.objects.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        default_program_photo = settings.DEFAULT_PROGRAM_IMAGE
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