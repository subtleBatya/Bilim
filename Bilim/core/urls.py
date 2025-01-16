from django.urls import path
from .views import *
app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("error/", error, name="error"),
    path("success/", success, name="success"),
]
