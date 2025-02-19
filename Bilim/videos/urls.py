from django.urls import path
from .views import *


app_name="videos"

urlpatterns = [
    path("technical_courses/", technical_courses, name="technical_courses"),
    path("natural_courses/",natural_courses, name="natural_courses"),
    path("humanitar_courses/",humanitar_courses, name="humanitar_courses"),
    path("video_of_course/<int:id>", video_of_course, name="video_of_course"),
    path("shorts/", shorts, name="shorts")
]
