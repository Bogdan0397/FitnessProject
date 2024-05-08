from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from fitness.models import Day
from lifestyle.models import FoodPlans


# Create your views here.
def lifestylehome(request):
    return render(request,'lifestyle/lifestyle_home.html')
class FoodPlansHome(ListView):
    template_name = 'lifestyle/foodplans_home.html'
    context_object_name = 'foodplans'
    allow_empty = False

    def get_queryset(self):
        return FoodPlans.objects.all()

class Foodplan(DetailView):
    template_name = 'lifestyle/foodplan.html'
    slug_url_kwarg = 'foodplan_slug'
    context_object_name = 'foodplan'

    def get_object(self):
        return get_object_or_404(FoodPlans,slug=self.kwargs[self.slug_url_kwarg])


