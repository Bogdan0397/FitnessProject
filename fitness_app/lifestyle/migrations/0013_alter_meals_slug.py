# Generated by Django 4.1.13 on 2024-05-22 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifestyle', '0012_meals_description_alter_meals_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
