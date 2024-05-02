
from django.contrib import admin
from .models import Workout, Programs, Exercises, Day


class ExercisesInline(admin.TabularInline):
    model = Day.exercises.through
    extra = 1  # Количество пустых форм для новых записей
    verbose_name = "Add Exercise"
    verbose_name_plural = "Add Exercises"


class DayInline(admin.StackedInline):
    model = Day
    extra = 1  # Количество пустых форм для новых записей
    inlines = [ExercisesInline]
    filter_horizontal = ('exercises',)

# Admin класс для Exercises
@admin.register(Exercises)
class Exercises(admin.ModelAdmin):
    list_display = ('name', 'slug', 'content')  # Отображаемые поля в списке
    search_fields = ('name',)  # Поля, по которым можно проводить поиск

# Admin класс для FoodPlans
@admin.register(Programs)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    exclude = ('exercises',)
    inlines = [DayInline]  # Добавление inline для дней

# Admin класс для Day
@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('name', 'program')
    list_filter = ('program',)
    search_fields = ('name',)
    inlines = [ExercisesInline]
    exclude = ('exercises',)
    filter_horizontal = ('exercises',)

# Admin класс для Lifestyle
@admin.register(Workout)
class LifestyleAdmin(admin.ModelAdmin):
    list_display = ('name', 'programs')
    search_fields = ('name',)
    list_filter = ('programs',)  # Фильтрация по планам питания