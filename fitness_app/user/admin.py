from django.apps import AppConfig
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User

admin.site.register(User,UserAdmin)

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


