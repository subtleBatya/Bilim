from django.urls import path
from .views import *

app_name = "users"


urlpatterns = [
    path("all/", all_users, name="all_users"),
    path("exact/<int:id>", exact_user, name="exact_user"),
    path("follow/<int:id>", follow, name="follow"),
    path("search_users/", search_users, name="search_users")
]