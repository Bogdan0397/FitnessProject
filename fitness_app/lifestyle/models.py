from django.db import models
from django.db import models
from django.urls import reverse


# Create your models here.

class Lifestyle(models.Model):
    foodplans = models.ForeignKey('FoodPlans',on_delete=models.PROTECT,related_name="food_plans",null=True, blank=True,verbose_name='FoodPlans')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)


class FoodPlans(models.Model):
    meals = models.ManyToManyField('Meals',related_name='meals',null=True, blank=True,verbose_name='Meals')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('lifestyle',kwargs={'foodplan_slug': self.slug})




class Meals(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('lifestyle',kwargs={'food_slug': self.slug})
