from django import template
from django.db.models import Count
from datetime import datetime

from lifestyle.models import Day

register = template.Library()

@register.inclusion_tag('lifestyle/list_days.html')
def foodplans_home(foodplan):
    days = Day.objects.filter(food_plan__slug=foodplan)
    return {'days':days}