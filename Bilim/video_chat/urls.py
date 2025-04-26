from django.urls import path
from .views import *
app_name = "video_chat"


urlpatterns = [
    path("", create_chat, name="create_chat"),
    path("chat/<str:room_name>/", room, name="room" ),
    path("get_token_for_chat_room/", getToken, name="get_token"),
    path("available_lessons/", available_lesson_for_student, name="available_lessons" ),
    path('create_lesson/', create_lesson, name='create_lesson'),
    path("get_username_by_uid/", get_username_by_uid, name="get_username_by_uid"),
    path("quit_user/", quit_user, name="quit_user")
]
