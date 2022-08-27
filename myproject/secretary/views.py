from django.shortcuts import render
from secretary.models import Secretary
from secretary.forms import ApplyForm
from django.http import HttpResponse  
from students.models import Student
from applies.models import Apply
from django.contrib.auth.decorators import login_required
from users.models import MyUser
from django.contrib.sites.shortcuts import get_current_site 
from django.template.loader import render_to_string  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes, force_text 
from django.core.mail import EmailMessage  

# Create your views here.

@login_required
def makeApply(request):
    if request.method == "POST":
        form = ApplyForm(request.POST)
        if form.is_valid():
            if Apply.objects.filter(status=3).exists():
                print(form.data['students'])
                apply = Apply.objects.get(student=form.data['students'])
                apply.status = form.data['status']
                apply.save()
                student = apply.student
                user = MyUser.objects.get(id=student.id+1)
                mail_subject = 'Apply evaluated'  
                message = render_to_string('apply_done.html', {  
                    'user': user,
                    'apply': apply,
                })  
                to_email = user.email
                email = EmailMessage(  
                            mail_subject, message, to=[to_email]  
                )  
                email.send()
                message ='Apply saved'
                return render(request,'secretary/makeapply.html',{'form': form,'message': message})
            else:
                message ='There is no applies'
                return render(request,'secretary/makeapply.html',{'form': form,'message': message})
    else:
        form = ApplyForm()
        applies = len(Apply.objects.filter(status=3))
        users = []
        if applies != 0:
            for apply in Apply.objects.filter(status=3):
                user = MyUser.objects.get(id=Student.objects.get(id=apply.student.id).user.id)
                student = Student.objects.get(user=user)
                users.append([user.id,user.email,user.first_name,user.last_name,student.studies,student.age,student.degree,student.course.name])
        return render(request,'secretary/makeapply.html',{'form': form,'users': users})
    return render(request,'secretary/makeapply.html',{'form': form})
