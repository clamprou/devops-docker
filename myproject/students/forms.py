from typing import Any
from django import forms  
from django.contrib.auth.forms import UserCreationForm 
from django.db import transaction
from students.models import Student
from django.contrib.auth import get_user_model
from courses.models import Course

class StudentSignUpForm(UserCreationForm):
    studies = forms.CharField(max_length=200, help_text='Required')
    age = forms.IntegerField(max_value=100, min_value=18, help_text='Required')
    degree = forms.IntegerField(max_value=10, min_value=0, help_text='Required')
    email = forms.EmailField(max_length=200, help_text='Required')
    course = forms.ChoiceField(choices=())
    class Meta(UserCreationForm.Meta):  
        model = get_user_model()
        fields = UserCreationForm.Meta.fields +('email', 'first_name', 'last_name','studies','age','degree','course')
    
    def __init__(self, *args, **kwargs):
            l = []
            for o in Course.objects.all():
                l.append((o.id, str(o.name)))
            asd = tuple(l)
            super().__init__(*args, **kwargs)
            
            self.fields['course'].choices = l