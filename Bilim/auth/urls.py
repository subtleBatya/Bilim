from django.urls import path
from .views import *

app_name = "auth"

urlpatterns = [
    path("login/", login, name="login"),
    path("sign_up/", sign_up, name="sign_up" ),
    path("payment/", payment, name="payment"),
    path("teacher_profile/", teacher_profile, name="teacher_profile"),
    path("teacher_create_video/", teacher_video_create, name="teacher_create_video")
]
