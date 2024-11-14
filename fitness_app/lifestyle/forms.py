from django import forms

from lifestyle.models import FoodPlans, Supplements, Supplement_Cat, Meals


class FoodPlanAdminForm(forms.ModelForm):
    class Meta:
        model = FoodPlans
        fields = ['name', 'slug', 'photo', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-input', 'cols': 60, 'rows': 10})
        }

class SupplementsAdminForm(forms.ModelForm):

    class Meta:
        model = Supplements
        fields = ['name', 'slug', 'photo', 'content','description','category']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-input', 'cols': 60, 'rows': 10})
        }

class SupplementsCatsAdminForm(forms.ModelForm):

    class Meta:
        model = Supplement_Cat
        fields = ['name', 'slug', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-input', 'cols': 60, 'rows': 10})
        }



class MealsAdminForm(forms.ModelForm):

    class Meta:
        model = Meals
        fields = ['name', 'slug', 'photo', 'content','description','calories','weight','carbs','fats','proteins']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-input', 'cols': 60, 'rows': 10})
        }