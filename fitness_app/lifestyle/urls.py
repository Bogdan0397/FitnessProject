from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from lifestyle import views
from lifestyle.views import lifestylehome, Foodplan, FoodPlansHome, DishView

urlpatterns = [
    path('lifestyle/',lifestylehome,name='lifestyle_home'),
    path('lifestyle/foodplans/',FoodPlansHome.as_view(), name='foodplans_home'),
    path('lifestyle/<slug:foodplan_slug>', Foodplan.as_view(),name='foodplan'),
    path('lifestyle/dish/<slug:dish_slug>', DishView.as_view(),name='dish')

]