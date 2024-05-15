from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from .models import Day
from .models import FoodPlans, Meals, Supplements
from . import views
from .utils import DataMixin


# Create your views here.
def lifestylehome(request):
    return render(request,'lifestyle/lifestyle_home.html',context={'selected_menu':'Life Style'})
class FoodPlansHome(DataMixin,ListView):
    template_name = 'lifestyle/foodplans_home.html'
    context_object_name = 'foodplans'
    allow_empty = False
    def get_queryset(self):
        self.qs = FoodPlans.objects.all()
        return self.qs


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        default_photo_foodplans_home = settings.DEFAULT_FOODPLAN_IMAGE
        return self.get_mixin_context(context, default_photo_foodplans_home=default_photo_foodplans_home)



class Foodplan(DataMixin,DetailView):
    template_name = 'lifestyle/foodplan.html'
    slug_url_kwarg = 'foodplan_slug'
    context_object_name = 'foodplan'

    def get_object(self):
        return get_object_or_404(FoodPlans,slug=self.kwargs[self.slug_url_kwarg])
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        default_photo_foodplan = settings.DEFAULT_FOODPLAN_IMAGE

        return self.get_mixin_context(context, default_photo_foodplan=default_photo_foodplan)


class DishView(DataMixin,DetailView):
    template_name = 'lifestyle/dish_detail.html'
    slug_url_kwarg = 'dish_slug'
    context_object_name = 'dish'

    def get_object(self):
        return get_object_or_404(Meals,slug=self.kwargs[self.slug_url_kwarg])
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        default_photo = settings.settings.DEFAULT_DISH_IMAGE
        return self.get_mixin_context(context, default_photo=default_photo)


class SupplementsHome(DataMixin,ListView):
    template_name = 'lifestyle/supp_home.html'
    context_object_name = 'supplements'
    allow_empty = False

    def get_queryset(self):
        return Supplements.objects.all()
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        default_photo = settings.DEFAULT_SUPP_IMAGE

        return self.get_mixin_context(context, default_photo=default_photo)


class SuppView(DataMixin,DetailView):
    template_name = 'lifestyle/supp_detail.html'
    slug_url_kwarg = 'supp_slug'
    context_object_name = 'supp'
    def get_object(self):
        return get_object_or_404(Supplements,slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        default_photo = settings.DEFAULT_SUPP_IMAGE

        return self.get_mixin_context(context, default_photo=default_photo)
