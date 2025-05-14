from django.urls import path
from .views import *

app_name = "applications"

urlpatterns = [
    path("", application, name="application"),
    path("api_application_get/", api_application, name="api_application"),
    path("api_application_create/", api_application_create, name="api_application_create")
]
