from django.urls import path
from .views import *

app_name = "applications"

urlpatterns = [
    path("", application, name="application")
]
