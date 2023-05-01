
from django.contrib import admin
from django.urls import path
from auapp.views import uhome,usignup,uwelcome,ulogout,urnp

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",uhome,name="uhome"),
    path("usignup",usignup,name="usignup"),
    path("uwelcome",uwelcome,name="uwelcome"),
    path("ulogout",ulogout,name="ulogout"),
    path("urnp",urnp,name="urnp"),
]
