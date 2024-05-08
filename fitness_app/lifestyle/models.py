from django.db import models
from django.db import models
from django.urls import reverse


# Create your models here.

class Lifestyle(models.Model):
    foodplans = models.ForeignKey('FoodPlans',on_delete=models.PROTECT,related_name="food_plans",null=True, blank=True,verbose_name='FoodPlans')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)


class FoodPlans(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    description = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('foodplan',kwargs={'foodplan_slug': self.slug})


class Meals(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('lifestyle',kwargs={'food_slug': self.slug})


class Day(models.Model):
    food_plan = models.ForeignKey('FoodPlans', on_delete=models.CASCADE, related_name='foodplan')
    name = models.CharField(max_length=100)
    meals = models.ManyToManyField('Meals', related_name='day_meals', blank=True)

    def __str__(self):
        return f"{self.name} ({self.food_plan.name})"

