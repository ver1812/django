from django.contrib import admin
from .models import WnModel
class WnAdmin(admin.ModelAdmin):
    list_display =("name","dt")
    list_filter = ("dt",)
admin.site.register(WnModel,WnAdmin)
