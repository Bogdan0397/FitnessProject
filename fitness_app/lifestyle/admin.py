from django.contrib import admin

from .forms import FoodPlanAdminForm, SupplementsAdminForm, SupplementsCatsAdminForm, MealsAdminForm
from .models import Lifestyle, FoodPlans, Meals, Day, Supplements, Supplement_Cat


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
    list_display = ('name', 'slug', 'description','photo')  # Отображаемые поля в списке
    search_fields = ('name',)  # Поля, по которым можно проводить поиск
    form = MealsAdminForm


# Admin класс для FoodPlans
@admin.register(FoodPlans)
class FoodPlansAdmin(admin.ModelAdmin):
    form = FoodPlanAdminForm
    list_display = ('name', 'slug','photo','goal','diet_type')
    fields = ('name', 'slug', 'photo', 'goal', 'diet_type','description')
    search_fields = ('name',)
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

@admin.register(Supplements)
class SupplyAdmin(admin.ModelAdmin):
    form = SupplementsAdminForm
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Supplement_Cat)
class SupplyCatAdmin(admin.ModelAdmin):
    form = SupplementsCatsAdminForm
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

