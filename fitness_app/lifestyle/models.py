from django.db import models
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Lifestyle(models.Model):
    foodplans = models.ForeignKey('FoodPlans',on_delete=models.PROTECT,related_name="food_plans",null=True, blank=True,verbose_name='FoodPlans')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)


class FoodPlans(models.Model):

    GOAL_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('maintenance', 'Maintenance'),
        ('weight_gain', 'Weight Gain'),
        ('muscle_gain', 'Muscle Gain'),
    ]

    DIET_TYPE_CHOICES = [
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('keto', 'Keto'),
        ('balanced', 'Balanced'),
        ('low_carb', 'Low Carb'),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    description = models.CharField(max_length=1500)
    photo = models.ImageField(upload_to='photos/foodplans',default=None,null=True,blank=True,verbose_name='Photo_Foodplan')

    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, default='maintenance')
    diet_type = models.CharField(max_length=20, choices=DIET_TYPE_CHOICES, default='balanced')
    def get_absolute_url(self):
        return reverse('foodplan',kwargs={'foodplan_slug': self.slug})


class Meals(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True)
    content = models.CharField(max_length=1500, blank=True)
    photo = models.ImageField(upload_to='photos/dish_photos',default=None,null=True,blank=True,verbose_name='Photo_Dish')
    calories = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    description = models.CharField(max_length=1500, blank=True)
    proteins = models.IntegerField(default=0)
    fats = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    def get_absolute_url(self):
        return reverse('dish',kwargs={'dish_slug': self.slug})



class Day(models.Model):
    food_plan = models.ForeignKey('FoodPlans', on_delete=models.CASCADE, related_name='foodplan')
    name = models.CharField(max_length=100)
    meals = models.ManyToManyField('Meals', related_name='day_meals', blank=True)

    def __str__(self):
        return f"{self.name} ({self.food_plan.name})"


class Supplements(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    description = models.CharField(max_length=250,null=True)
    content = models.CharField(max_length=1500, blank=True)
    photo = models.ImageField(upload_to='photos/supplement_photos', default=None, null=True, blank=True,
                              verbose_name='Photo_Supp')
    category = models.ForeignKey('Supplement_Cat', on_delete=models.SET_NULL, null=True, blank=True, related_name='supp_cat',
                                   verbose_name="Supplement_category")

    def get_absolute_url(self):
        return reverse('supp',kwargs={'supp_slug': self.slug})


class Supplement_Cat(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Meals)
def add_id_to_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = f'{slugify(instance.slug)}-{instance.id}'
        instance.save()