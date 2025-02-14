from django.contrib import admin
from .models import *
# Register your models here.
class AdminVideoCourse(admin.ModelAdmin):
    list_display = ("title", 'category', 'course', 'views', 'author', "accepted")
admin.site.register(VideoCourse, AdminVideoCourse)
admin.site.register(Video_course)
admin.site.register(Video_category)