from django.contrib import admin
from .models import FbModel

class FbAdmin(admin.ModelAdmin):
    list_display=("name","dt")
    list_filter=("name","dt")
admin.site.register(FbModel,FbAdmin)

# Register your models here.
