from django.contrib.auth.models import AbstractUser
from django.db import models


class Status(models.IntegerChoices):
    MAN = 0, 'Чоловік'
    WOMAN = 1, 'Жінка'
class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d',blank = True,null=True,verbose_name='Фото')
    date_birth = models.DateTimeField(blank=True,null=True,verbose_name='Дата народження')
    weight = models.FloatField(blank=True,null=True,verbose_name='Маса тіла')
    height = models.FloatField(blank=True,null=True,verbose_name='Зріст')
    gender = models.BooleanField(choices=tuple(map(lambda x:(bool(x[0]),x[1]),Status.choices)),
                                 default=Status.MAN, verbose_name="Стать")


