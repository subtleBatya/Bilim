from django.urls import path
from .views import *


app_name = "teacher"

urlpatterns = [
    path("", teacher_profile, name="teacher_profile"),
    path("create_video/", teacher_video_create, name="teacher_video_create")
]
