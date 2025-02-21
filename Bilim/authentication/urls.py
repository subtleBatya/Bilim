from django.urls import path
from .views import *

app_name = "auth"

urlpatterns = [
    path("login/", login, name="login"),
    path("sign_up/", sign_up, name="sign_up" ),
    path("logout/", logout, name="logout"),
    path("payment/", payment, name="payment"),
    path("profile/", profile, name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("custom_admin/", admin_page, name="admin_page"),
    path("video_admin/<int:id>", admin_video, name="admin_video"),
    path("accept_video/<int:id>", accept_video, name="accept_video")
]
