from django.shortcuts import render
from .forms import EnForm
from .models import EnModel

def home(request):
    if request.method=="POST":
        data =EnForm(request.POST)
        data.save()
        msg = "we will get back to you "
        fm = EnForm()
        return render(request,"home.html",{"fm":fm,"msg":msg})
    else:
        fm = EnForm()
        return render(request,"home.html",{"fm":fm})
        

