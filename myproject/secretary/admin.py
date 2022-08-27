from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from secretary.models import Secretary

# # Register your models here.from django.contrib.auth import get_user_model
admin.site.register(Secretary)