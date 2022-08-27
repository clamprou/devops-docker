from django import forms
from applies.models import Apply
from students.models import Student

class ApplyForm(forms.Form): 
    APPLY_CHOICES =(
    ("1", "Aproved"),
    ("2", "Dissaproved"),
    )
    status = forms.ChoiceField(choices=APPLY_CHOICES)
    students = forms.ChoiceField(choices=(), required=True, widget=forms.RadioSelect)
    def __init__(self, *args, **kwargs):
        l = []
        for o in Apply.objects.filter(status=3):
            l.append((o.student.id,str(o.student.user)+" "+str(o.student.user.email)))
        students = None
        if len(kwargs):
            students = kwargs.pop('students')
        super().__init__(*args, **kwargs)
        
        self.fields['students'].choices = l