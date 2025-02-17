from django.urls import path
from .views import *

app_name = 'library'

urlpatterns = [
    path("", library, name="library"),
    path("details/<int:id>", book_details, name="book_details")
]
