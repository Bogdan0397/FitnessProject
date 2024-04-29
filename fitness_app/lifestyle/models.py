from django.db import models

# Create your models here.

class Lifestyle(models.Model):
    subcategories = models.ForeignKey(name="sub_categories")
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)



class FoodPlans(models.Model):
    meals = models.ManyToManyField()
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)




class Meals(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.CharField(max_length=100, blank=True)