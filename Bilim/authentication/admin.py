from django.contrib import admin
from .models import *
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "telephone_number")
    list_filter = ("username",)

admin.site.register(User)