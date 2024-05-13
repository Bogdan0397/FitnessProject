from django import template
from django.db.models import Count
from datetime import datetime

from fitness.models import Day

register = template.Library()

@register.inclusion_tag('fitness/list_days.html')
def programs_home(program):
    days = Day.objects.filter(program__slug=program)
    return {'days':days}