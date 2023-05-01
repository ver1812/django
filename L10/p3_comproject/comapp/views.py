from django.shortcuts import render
from folium import *
from geocoder import *

def home(request):
    if request.GET.get("city"):
        city = request.GET.get("city")
        try:
            data = osm(city)
            loc =[data.lat,data.lng]
            

