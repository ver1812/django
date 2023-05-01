from django.shortcuts import render
from .models import StudentModel
from .forms import StudentForm
from django.core.mail import send_mail

def home(request):
    if request.method =="POST" and request.POST.get("b1"):
        em = request.POST.get("email")
        try:
            usr = StudentModel.objects.get(email=em)
            fm = StudentForm()
            return render(request,"home.html",{"msg":"email already registered ","fm":fm})
        except StudentModel.DoesNotExist:
            data = StudentForm(request.POST)
            data.save()
            fm = StudentForm()
            subject = "Welcome to kamal Classes"
            text = "congrats for subscription"
            from_email = "vighneshsadvilkar2@gmail.com"
            to_email = [str(em)]
            send_mail(subject,text,from_email,to_email)
            return render(request,"home.html",{"msg":"email registered ","fm":fm})
    elif request.method =="POST" and request.POST.get("b2"):
        em = request.POST.get("email")
        try:
            usr = StudentModel.objects.get(email=em)
            usr.delete()
            fm = StudentForm()
            subject = "Welcome to kamal Classes"
            text = "sorry for unsubs"
            from_email = "vighneshsadvilkar2@gmail.com"
            to_email = [str(em)]
            send_mail(subject,text,from_email,to_email)
            return render(request,"home.html",{"msg":"email unregistered ","fm":fm})
        except StudentModel.DoesNotExist:
            fm = StudentForm()
            return render(request,"home.html",{"msg":"email not registered ","fm":fm})
    else:
        fm = StudentForm()
        return render(request,"home.html",{"fm":fm})






