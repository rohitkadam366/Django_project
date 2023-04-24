from django.shortcuts import render
from enroll.models import student
from .Forms import loginForm
# Create your views here.

def studentinfo(request):
    stu = student.objects.all()
    return render(request,'enroll/studentinfo.html',{'stud':stu})

def LoginForm(request):
    log = loginForm(auto_id=True,label_suffix='$')
    return render(request,'enroll/LoginForm.html',{'form':log})