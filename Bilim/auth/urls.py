from django.urls import path
from .views import *

app_name = "auth"

urlpatterns = [
    path("login/", login, name="login"),
    path("sign_up/", sign_up, name="sign_up" ),
    path("payment/", payment, name="payment")
]
