from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from fitness.models import Day
from lifestyle.models import FoodPlans, Meals, Supplements


# Create your views here.
def lifestylehome(request):
    return render(request,'lifestyle/lifestyle_home.html')
class FoodPlansHome(ListView):
    template_name = 'lifestyle/foodplans_home.html'
    context_object_name = 'foodplans'
    allow_empty = False
    extra_context = {'default_foodplan_photo': settings.DEFAULT_FOODPLAN_IMAGE}
    def get_queryset(self):
        return FoodPlans.objects.all()

class Foodplan(DetailView):
    template_name = 'lifestyle/foodplan.html'
    slug_url_kwarg = 'foodplan_slug'
    context_object_name = 'foodplan'
    extra_context = {'default_foodplan_photo': settings.DEFAULT_FOODPLAN_IMAGE}
    def get_object(self):
        return get_object_or_404(FoodPlans,slug=self.kwargs[self.slug_url_kwarg])



class DishView(DetailView):
    template_name = 'lifestyle/dish_detail.html'
    slug_url_kwarg = 'dish_slug'
    context_object_name = 'dish'
    extra_context = {'dish_photo_default':settings.DEFAULT_DISH_IMAGE}
    def get_object(self):
        return get_object_or_404(Meals,slug=self.kwargs[self.slug_url_kwarg])


class SupplementsHome(ListView):
    template_name = 'lifestyle/supp_home.html'
    context_object_name = 'supplements'
    allow_empty = False
    extra_context = {'supp_photo_default': settings.DEFAULT_SUPP_IMAGE}
    def get_queryset(self):
        return Supplements.objects.all()


class SuppView(DetailView):
    template_name = 'lifestyle/supp_detail.html'
    slug_url_kwarg = 'supp_slug'
    context_object_name = 'supp'
    extra_context = {'supp_photo_default':settings.DEFAULT_SUPP_IMAGE}
    def get_object(self):
        return get_object_or_404(Supplements,slug=self.kwargs[self.slug_url_kwarg])