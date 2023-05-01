from django.shortcuts import render
from folium import*

def home(request):
    return render(request,"home.html")

def locate(request):
    loc = [19.0188808,73.0287206]
    f = Figure(width=500,height=500)
    thane = Map(location=loc,zoom_start=18).add_to(f)
    Marker(loc,tooltip='<b>KC Thane</b>',popup="<b>Kamal Classes</b>").add_to(thane)
    thane_html =thane._repr_html_()
    return render(request,"locate.html",{"msg":thane_html})
