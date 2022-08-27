from django.db import models
from django.conf import settings
from courses.models import Course
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.signals import setting_changed
from django.contrib.auth import get_user_model
from django.apps import apps


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=None)
    studies = models.CharField(default="None", max_length=200)
    age = models.IntegerField(default=0)
    degree = models.FloatField(default=0)
    course = models.ForeignKey(default= None,to=Course, on_delete=models.CASCADE)

    @classmethod
    def create(cls, user, studies, age, degree, course):
        student = cls(user=user,studies=studies,age=age,degree=degree,course=course)
        # do something with the book
        return student

    def __str__(self):
        return str(self.id)