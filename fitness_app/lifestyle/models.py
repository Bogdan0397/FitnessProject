from django.db import models

# Create your models here.

class Lifestyle(models.Model):
    subcategories = models.ForeignKey()
    name = models.CharField(max_length=100)
    slug = models.SlugField()



class FoodPlans(models.Model):
    meals = models.ManyToManyField()
    name = models.CharField(max_length=100)
    slug = models.SlugField()




class Meals(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.CharField(max_length)