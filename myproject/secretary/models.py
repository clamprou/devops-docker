from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class Secretary(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)

    @classmethod
    def create(cls, user):
        secretary = cls(user=user)
        # do something with the apply
        return secretary

    def __str__(self):
        return str(self.user)

