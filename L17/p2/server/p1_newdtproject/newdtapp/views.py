from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import *

@api_view(["GET"])
def dt(request):
    d = datetime.now().date()
    msg = "Server date = " + str(d)
    return Response({"msg":msg})

@api_view(["GET"])
def ti(request):
    d = datetime.now().time()
    msg = "Server time = " + str(d)
    return Response({"msg":msg})

@api_view(["GET"])
def dtti(request):
    d = datetime.now()
    msg = "Server date  and time = " + str(d)
    return Response({"msg":msg})



