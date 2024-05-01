from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('lifestyle/',views.lifestyle_home, name='lifestyle_home'),
    path('lifestyle/<slug:foodplan_slug>', views.home,name='article'),
    path('lifestyle/<slug:food_slug>', views.home,name='dish')

]