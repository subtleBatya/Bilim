from django.urls import path
from .views import *

app_name = "users"


urlpatterns = [
    path("all/", all_users, name="all_users"),
    path("exact/<int:id>", exact_user, name="exact_user")
]