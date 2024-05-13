
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from fitness import views
urlpatterns = [
    path('', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('about/ourteam/',views.about,name='our_team'),
    path('about/contact/',views.contact,name='contact'),
    path('workout/<slug:program_slug>', views.home,name='program'),
    path('workout/<slug:exercise_slug>', views.home,name='exercise')
]