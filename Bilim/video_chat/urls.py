from django.urls import path
from .views import *
app_name = "video_chat"


urlpatterns = [
    path("", create_chat, name="create_chat"),
    path("chat/<str:room_name>/", room, name="room" ),
    path("get_token_for_chat_room/", getToken, name="get_token")
]
