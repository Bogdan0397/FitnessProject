# Generated by Django 4.1.13 on 2024-05-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifestyle', '0002_remove_foodplans_meals'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodplans',
            name='description',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
