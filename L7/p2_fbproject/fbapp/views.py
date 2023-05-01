from django.shortcuts import render
from .forms import FbForm
from .models import FbModel

def home(request):
    if request.method=="POST":
        data =FbForm(request.POST)
        data.save()
        msg = "we will get back to you "
        fm = FbForm()
        return render(request,"home.html",{"fm":fm,"msg":msg})
    else:
        fm = FbForm()
        return render(request,"home.html",{"fm":fm})

# Create your views here.
