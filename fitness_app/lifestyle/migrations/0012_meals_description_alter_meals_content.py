# Generated by Django 4.1.13 on 2024-05-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifestyle', '0011_meals_calories_meals_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='description',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='meals',
            name='content',
            field=models.CharField(blank=True, max_length=1500),
        ),
    ]
