from django.urls import path
from .views import *


app_name="videos"

urlpatterns = [
    path("courses/<int:id>", all_courses, name="all_courses"),
    path("video_of_course/<int:id>", video_of_course, name="video_of_course"),
    path("shorts/", shorts, name="shorts"),
    path("shorts/<int:id>/", user_shorts, name="user_shorts"),
    path("create_shorts/", create_shorts, name="create_shorts"),
    path("like-video/<int:video_id>/", like_video, name="like_video"),
]
