from django.urls import path
from .views import *

app_name = "auth"

urlpatterns = [
    path("login/", login, name="login"),
    path("sign_up/", sign_up, name="sign_up" ),
    path("logout/", logout, name="logout"),
    path("payment/", payment, name="payment"),
    path("custom_admin/", admin_page, name="admin_page"),
    path("profile/", profile, name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile")
]
