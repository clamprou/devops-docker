from django.shortcuts import render
from django.shortcuts import render 
from students.models import Student
from applies.models import Apply

def apply(request):
    current_user = request.user
    apply = Apply.objects.get(student=Student.objects.get(user=current_user))
    if apply.status == '1':
        data = "Approved"
    elif apply.status == '2':
        data = "Disapproved"
    else:
        data = "Pending"
    student = Student.objects.get(user=current_user)
    context = {'data' : data}
    return render(request,'students/apply.html',{'data': data,'student': student,'user':current_user})
