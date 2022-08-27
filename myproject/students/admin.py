from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from students.models import Student

# # Register your models here.from django.contrib.auth import get_user_model
admin.site.register(Student)