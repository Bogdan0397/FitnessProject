# Generated by Django 4.1.13 on 2025-06-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0007_exercises_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='programs',
            name='difficulty',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=20),
        ),
        migrations.AddField(
            model_name='programs',
            name='duration',
            field=models.CharField(choices=[('short', 'Up to 4 weeks'), ('medium', '4 to 8 weeks'), ('long', 'More than 8 weeks')], default='medium', max_length=20),
        ),
        migrations.AddField(
            model_name='programs',
            name='goal',
            field=models.CharField(choices=[('strength', 'Build Strength'), ('endurance', 'Improve Endurance'), ('weight_loss', 'Weight Loss'), ('mobility', 'Mobility & Flexibility')], default='strength', max_length=20),
        ),
    ]
