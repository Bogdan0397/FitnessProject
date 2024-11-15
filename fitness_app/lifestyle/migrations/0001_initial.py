# Generated by Django 4.1.13 on 2024-05-07 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('content', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lifestyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('foodplans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='food_plans', to='lifestyle.foodplans', verbose_name='FoodPlans')),
            ],
        ),
        migrations.AddField(
            model_name='foodplans',
            name='meals',
            field=models.ManyToManyField(blank=True, null=True, related_name='meals', to='lifestyle.meals', verbose_name='Meals'),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('food_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='lifestyle.foodplans')),
                ('meals', models.ManyToManyField(blank=True, related_name='day_meals', to='lifestyle.meals')),
            ],
        ),
    ]
