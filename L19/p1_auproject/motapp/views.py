
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import *

mm = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
]

@api_view(["GET"])
def motmsg(request):
    r = randint(0,len(mm)-1)
    msg = mm[r]
    return Response({"msg":msg})
