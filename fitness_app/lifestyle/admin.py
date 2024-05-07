from django.contrib import admin
from .models import Lifestyle, FoodPlans, Meals, Day

# Inline класс для отображения модели Meals внутри Day

class MealsInline(admin.TabularInline):
    model = Day.meals.through
    extra = 1  # Количество пустых форм для новых записей
    verbose_name = "Add Meal"
    verbose_name_plural = "Add Meals"

# Inline класс для отображения дней внутри плана питания
class DayInline(admin.TabularInline):
    model = Day
    extra = 1  # Количество пустых форм для новых записей
    filter_horizontal = ('meals',)

# Admin класс для Meals
@admin.register(Meals)
class MealsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'content')  # Отображаемые поля в списке
    search_fields = ('name',)  # Поля, по которым можно проводить поиск

# Admin класс для FoodPlans
@admin.register(FoodPlans)
class FoodPlansAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    exclude = ('meals',)
    inlines = [DayInline]  # Добавление inline для дней

# Admin класс для Day
@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('name', 'food_plan')
    list_filter = ('food_plan',)
    search_fields = ('name',)
    inlines = [MealsInline]
    filter_horizontal = ('meals',)

# Admin класс для Lifestyle
@admin.register(Lifestyle)
class LifestyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'foodplans')
    search_fields = ('name',)
    list_filter = ('foodplans',)  # Фильтрация по планам питания