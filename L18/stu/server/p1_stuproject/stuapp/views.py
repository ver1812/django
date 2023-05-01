from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import StudentModel
from .ser import StudentSerializer

@api_view(["POST","GET"])
def stuop(request):
    if request.method == "POST":
        record = StudentSerializer(data=request.data)
        if record.is_valid():
            record.save()
            return Response({"msg":"record created "})
        else:
            return Response(record.errors)
    elif request.method == "GET":
        result = StudentModel.objects.all()
        sresult = StudentSerializer(result,many=True)
        print(sresult.data)
        return Response(sresult.data)
    

