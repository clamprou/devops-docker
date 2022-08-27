from django.db import models
from secretary.models import Secretary
from students.models import Student

# Create your models here.

class Apply(models.Model):
    APPLY_CHOICES =(
    ("1", "Aproved"),
    ("2", "Dissaproved"),
    ("3", "Pending")
    )
    status = models.CharField(default="Pending", max_length=30,choices=APPLY_CHOICES)
    student = models.OneToOneField(default= None,to=Student, on_delete=models.CASCADE)
    secretary = models.ForeignKey(default= None,to=Secretary,on_delete=models.CASCADE)

    @classmethod
    def create(cls, status, student, secretary):
        apply = cls(status=status,student=student,secretary=secretary)
        # do something with the apply
        return apply


    def __str__(self):
        return str(self.id)