from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(default="None", max_length=30)
    
    def __str__(self):
        return str(self.name)