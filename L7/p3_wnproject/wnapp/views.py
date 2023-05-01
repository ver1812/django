from django.shortcuts import render
from .forms import WnForm
from .models import WnModel

def home(request):
    if request.method=="POST":
        data =WnForm(request.POST)
        data.save()
        msg = "we will get back to you "
        fm = WnForm()
        return render(request,"home.html",{"fm":fm,"msg":msg})
    else:
        fm = WnForm()
        return render(request,"home.html",{"fm":fm})
