from django.contrib import admin
from .models import StudentModel

class StudentAdmin(admin.ModelAdmin):
    list_display = ("email","dt")
    list_filter = ("dt",)


admin.site.register(StudentModel,StudentAdmin)

