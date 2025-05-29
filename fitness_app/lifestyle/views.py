from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from .models import Day
from .models import FoodPlans, Meals, Supplements
from . import views, models
from .utils import DataMixin
from django.db.models import Q


# Create your views here.
def lifestylehome(request):

    q1 = FoodPlans.objects.all()
    q2 = Supplements.objects.all()
    return render(request,'lifestyle/lifestyle_home.html',context={'selected_menu':'Life Style',
                                                                   'foodplans':q1,'supplements':q2})
class FoodPlansHome(DataMixin,ListView):
    template_name = 'lifestyle/foodplans_home.html'
    context_object_name = 'foodplans'
    allow_empty = True

    def get_queryset(self):
        query = self.request.GET.get('q')
        goal = self.request.GET.get('goal')
        diet_type = self.request.GET.get('diet_type')

        qs = FoodPlans.objects.all()
        if query:
            qs = qs.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if goal:
            qs = qs.filter(goal=goal)
        if diet_type:
            qs = qs.filter(diet_type=diet_type)
        return qs


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['foodplan_goals'] = FoodPlans.GOAL_CHOICES
        context['foodplan_diet_types'] = FoodPlans.DIET_TYPE_CHOICES
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

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        program = self.get_object()
        user = request.user

        user.selected_nutrition_program = program
        user.save()

        return redirect('user:profile')


class DishView(DataMixin,DetailView):
    template_name = 'lifestyle/dish_detail.html'
    slug_url_kwarg = 'dish_slug'
    context_object_name = 'dish'

    def get_object(self):
        return get_object_or_404(Meals,slug=self.kwargs[self.slug_url_kwarg])
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        default_photo_dish = settings.DEFAULT_DISH_IMAGE
        return self.get_mixin_context(context, default_photo_dish=default_photo_dish)


class SupplementsHome(DataMixin,ListView):
    template_name = 'lifestyle/supp_home.html'
    context_object_name = 'supplements'
    allow_empty = False

    def get_queryset(self):
        return Supplements.objects.all()
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        default_photo_supp = settings.DEFAULT_SUPP_IMAGE

        return self.get_mixin_context(context, default_photo_supp=default_photo_supp)


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
