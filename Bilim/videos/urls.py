from django.urls import path
from .views import *


app_name="videos"

urlpatterns = [
    path("courses/", courses, name="courses"),
    path("video_of_course/", video_of_course, name="video_of_course")
]
