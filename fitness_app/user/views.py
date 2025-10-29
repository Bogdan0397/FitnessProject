from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm
from datetime import date


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')



class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'user/profile.html'

    today = date.today().weekday()  # 0 = Monday, 6 = Sunday
    today_name = date.today().strftime('%A')  # Наприклад, 'Tuesday'

    def get_success_url(self):
        return reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user
    #check commit#
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['nutrition_program'] = user.selected_nutrition_program
        context['fitness_program'] = user.selected_fitness_program

        if user.height and user.weight:
            weight = user.weight
            height = user.height
            age = 30  # або user.age, якщо є таке поле
            bmr = int(66 + (13.7 * weight) + (5 * height) - (6.8 * age))
            context['calories'] = {
                'maintenance': bmr,
                'loss': bmr - 500,
                'gain': bmr + 500,
            }

        return context
