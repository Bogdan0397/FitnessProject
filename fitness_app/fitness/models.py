from django.db import models
from django.urls import reverse
# Create your models here.
class Workout(models.Model):
    programs = models.ForeignKey('Programs',on_delete=models.PROTECT,related_name="programs",null=True, blank=True,verbose_name='Programs')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

class Programs(models.Model):
    exercises = models.ManyToManyField('Exercises', related_name='exercises', blank=True, verbose_name='Exercises')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    photo = models.ImageField(upload_to='photos/programs', default=None, null=True, blank=True,
                              verbose_name='Photo_Program')
    description = models.TextField(max_length=250,null=True)
    def get_absolute_url(self):
        return reverse('program',kwargs={'program_slug': self.slug})

class Exercises(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='photos/exercises', default=None, null=True, blank=True,
                              verbose_name='Photo_Exercise')
    def get_absolute_url(self):
        return reverse('exercise',kwargs={'exercise_slug': self.slug})

class Day(models.Model):
    program = models.ForeignKey('Programs', on_delete=models.CASCADE, related_name='days_train')
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField('Exercises', related_name='day_exercises', blank=True)

    def __str__(self):
        return f"{self.name} ({self.program.name})"

