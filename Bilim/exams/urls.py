from django.urls import path
from .views import *

app_name = "exams"

urlpatterns = [
    path("", user_exams, name="user_exams")
]
