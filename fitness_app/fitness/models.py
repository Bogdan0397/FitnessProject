from django.db import models
from django.urls import reverse
# Create your models here.
class Workout(models.Model):
    programs = models.ForeignKey('Programs',on_delete=models.PROTECT,related_name="programs",null=True, blank=True,verbose_name='Programs')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

class Programs(models.Model):

    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    DURATION_CHOICES = [
        ('short', 'Up to 4 weeks'),
        ('medium', '4 to 8 weeks'),
        ('long', 'More than 8 weeks'),
    ]

    GOAL_CHOICES = [
        ('strength', 'Build Strength'),
        ('endurance', 'Improve Endurance'),
        ('weight_loss', 'Weight Loss'),
        ('mobility', 'Mobility & Flexibility'),
    ]

    exercises = models.ManyToManyField('Exercises', related_name='exercises', blank=True, verbose_name='Exercises')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    photo = models.ImageField(upload_to='photos/programs', default=None, null=True, blank=True,
                              verbose_name='Photo_Program')
    description = models.TextField(max_length=250,null=True)

    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='beginner')
    duration = models.CharField(max_length=20, choices=DURATION_CHOICES, default='medium')
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES, default='strength')

    def get_absolute_url(self):
        return reverse('program',kwargs={'program_slug': self.slug})

class Exercises(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='photos/exercises', default=None, null=True, blank=True,
                              verbose_name='Photo_Exercise')
    repetitions = models.IntegerField(default=0)
    times = models.IntegerField(default=0)
    video_link = models.URLField(max_length=200,null=True)

    def save(self, *args, **kwargs):
        if self.video_link:
            # Извлечение идентификатора видео из ссылки на YouTube
            start_index = self.video_link.find('=') + 1
            end_index = self.video_link.find('&')
            if end_index == -1:
                end_index = None
            video_id = self.video_link[start_index:end_index]

            # Сохранение идентификатора видео в поле
            self.video_link = video_id

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('exercise',kwargs={'exercise_slug': self.slug})

class Day(models.Model):
    program = models.ForeignKey('Programs', on_delete=models.CASCADE, related_name='days_train')
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField('Exercises', related_name='day_exercises', blank=True)

    def __str__(self):
        return f"{self.name} ({self.program.name})"

