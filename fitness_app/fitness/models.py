from django.db import models
from django.urls import reverse
# Create your models here.
class Workout(models.Model):
    programs = models.ForeignKey('Programs',on_delete=models.PROTECT,related_name="programs",null=True, blank=True,verbose_name='Programs')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

class Programs(models.Model):
    exercises = models.ManyToManyField('Exercises', related_name='exercises', null=True, blank=True, verbose_name='Exercises')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('workout',kwargs={'program_slug': self.slug})

class Exercises(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.CharField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('workout',kwargs={'exercise_slug': self.slug})