from django.contrib.auth.models import AbstractUser
from django.db import models


class Status(models.IntegerChoices):
    MAN = 0, 'Man'
    WOMAN = 1, 'Woman'

class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank = True,null=True,verbose_name='Фото')
    date_birth = models.DateTimeField(blank=True,null=True,verbose_name='Дата народження')
    weight = models.FloatField(blank=True,null=True,verbose_name='Маса тіла')
    height = models.FloatField(blank=True,null=True,verbose_name='Зріст')
    gender = models.BooleanField(choices=tuple(map(lambda x:(bool(x[0]),x[1]),Status.choices)),
                                 default=Status.MAN, verbose_name="Стать")


    selected_nutrition_program = models.ForeignKey(
        'lifestyle.FoodPlans',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='users_nutrition',
        limit_choices_to={'program_type': 'nutrition'},
        verbose_name="Food Plan"
    )

    selected_fitness_program = models.ForeignKey(
        'fitness.Programs',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='users_fitness',
        limit_choices_to={'program_type': 'fitness'},
        verbose_name="Fitness-Program"
    )