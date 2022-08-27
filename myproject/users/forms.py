from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MyUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserCreationForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser

