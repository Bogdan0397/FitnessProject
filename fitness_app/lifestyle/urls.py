from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from fitness import views

urlpatterns = [
    path('lifesytle/<slug:foodplan_slug>', views.home,name='article'),
    path('lifesytle/<slug:food_slug>', views.home,name='dish')

]