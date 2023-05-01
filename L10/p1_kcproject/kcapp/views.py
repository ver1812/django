from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def python(request):
    return render(request,"python.html")

def ml(request):
    return render(request,"ml.html")

def jsmern(request):
    return render(request,"jsmern.html")

def django(request):
    return render(request,"django.html")

