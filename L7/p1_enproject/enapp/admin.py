from django.contrib import admin
from .models import EnModel

class EnAdmin(admin.ModelAdmin):
    list_display=("name","dt")
    list_filter = ("dt",)
admin.site.register(EnModel,EnAdmin)

# Register your models here.
