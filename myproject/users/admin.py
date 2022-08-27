from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MyUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.admin import UserAdmin
class MyUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_secretary',)}),
    )

admin.site.register(MyUser, MyUserAdmin)