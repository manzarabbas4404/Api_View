from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(students)
class student_apiAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','city']