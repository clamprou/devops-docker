from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from applies.models import Apply

# # Register your models here.from django.contrib.auth import get_user_model
admin.site.register(Apply)