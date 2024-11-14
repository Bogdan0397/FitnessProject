
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

from .views import workouthome, ProgramsHome, Program, ExerciseView

urlpatterns = [
    path('', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('about/ourteam/',views.about,name='our_team'),
    path('about/contact/',views.contact,name='contact'),
    path('workout/',workouthome,name='workout_home'),
    path('workout/programs/',ProgramsHome.as_view(), name='programs_home'),
    path('workout/<slug:program_slug>', Program.as_view(),name='program'),
    path('workout/exercise/<slug:exercise_slug>', ExerciseView.as_view(),name='exercise'),
]