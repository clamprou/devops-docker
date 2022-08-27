
# from xmlrpc.client import DateTime
# from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save
# from django.apps import apps
# from django.contrib.auth import get_user_model
# from django.core.signals import setting_changed
# from django.dispatch import receiver
# from datetime import datetime
# from django import forms
# from django.template import loader
# from django.core.mail import EmailMultiAlternatives
# from courses.models import Course

# def post_save_receiver(sender, instance, created, **kwargs):
#     pass

# post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)

# @receiver(setting_changed)
# def user_model_swapped(**kwargs):
#     if kwargs['setting'] == 'AUTH_USER_MODEL':
#         apps.clear_cache()


# class Student(AbstractUser):
#     studies = models.CharField(default="None", max_length=30)
#     age = models.IntegerField(default=0)
#     degree = models.FloatField(default=0)
#     course = models.ForeignKey(default= None,to=Course, on_delete=models.CASCADE,null=True)
#     APPLY_CHOICES =(
#     ("1", "Aproved"),
#     ("2", "Dissaproved"),
#     )
#     apply = models.CharField(default="Pending", max_length=30,choices=APPLY_CHOICES)

class MyUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
    # REQUIRED_FIELDS = ['is_student', 'is_secretary']


    def __str__(self):
        return str(self.id)
