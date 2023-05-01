
from django.contrib import admin
from django.urls import path
from kcapp.views import home,python,ml,jsmern,django

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("python",python,name="python"),
    path("ml",ml,name="ml"),
    path("jsmern",jsmern,name="jsmern"),
    path("django",django,name="django"),

]
