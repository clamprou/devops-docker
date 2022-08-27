from django.shortcuts import render
from students.forms import StudentSignUpForm
from django.http import HttpResponse  
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from django.core.mail import EmailMessage 
from .token import account_activation_token  
from django.contrib.auth import get_user_model
from students.models import Student
from courses.models import Course
from applies.models import Apply
from secretary.models import Secretary

def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.is_active = False
            user.save()
            student = Student.create(user,form.data['studies'],form.data['age'],form.data['degree'],Course.objects.get(id=form.data['course']))
            student.save()
            apply = Apply.create(3,student,Secretary.objects.get(user=1))
            apply.save()
            current_site = get_current_site(request) 
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return render(request,'users/email_conf.html')
    else:
        form = StudentSignUpForm()
    return render(request,'users/register.html',{'form': form})

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True 
        user.save()
        return render(request,'users/email_succ.html') 
    else:  
        return HttpResponse('Activation link is invalid!')

