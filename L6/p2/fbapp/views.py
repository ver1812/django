from django.shortcuts import render
from .forms import FbForm 
from .models import FbModel

def home(request):
    if request.method=="POST":
        na = request.POST.get("name")
        fb = request.POST.get("feedback")
        data = FbModel(name = na ,feedback =fb)
        data.save()
        msg = "Thank you for your feedback "
        fm =FbForm()
        return render(request,"home.html",{"fm":fm,"msg":msg})
    else:
        fm =FbForm()
        return render(request,"home.html",{"fm":fm})

# Create your views here.
