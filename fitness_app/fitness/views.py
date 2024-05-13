from django.shortcuts import render
from django.conf import settings
from fitness.models import Programs, Exercises
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
def home(request):
    return render(request,'fitness/home.html')

def about(request):
    return render(request,'fitness/about.html',context={'selected_menu':'About'})

def contact(request):
    return render(request,'fitness/contact.html',context={'selected_menu':'About'})

def workouthome(request):
    return render(request, 'fitness/workout_home.html')

class ProgramsHome(ListView):
    template_name = 'fitness/programs_home.html'
    context_object_name = 'programs'
    allow_empty = False
    extra_context = {'default_program_photo': settings.DEFAULT_PROGRAM_IMAGE}
    def get_queryset(self):
        return Programs.objects.all()

class Program(DetailView):
    template_name = 'fitness/program.html'
    slug_url_kwarg = 'program_slug'
    context_object_name = 'program'
    extra_context = {'default_program_photo': settings.DEFAULT_PROGRAM_IMAGE}
    def get_object(self):
        return get_object_or_404(Programs,slug=self.kwargs[self.slug_url_kwarg])

class ExerciseView(DetailView):
    template_name = 'fitness/exercise_detail.html'
    slug_url_kwarg = 'exercise_slug'
    context_object_name = 'exercise'
    extra_context = {'default_exercise_image':settings.DEFAULT_EXRCISE_IMAGE}

    def get_object(self):
        return get_object_or_404(Exercises, slug=self.kwargs[self.slug_url_kwarg])