from django.urls import path
from .views import *


app_name = "teacher"

urlpatterns = [
    path("", teacher_profile, name="teacher_profile"),
    path("content/", teacher_content, name="teacher_content"),
    path("create/", teacher_video_create, name="teacher_video_create"),
    path("edit/", teacher_edit, name="teacher_edit")
]
