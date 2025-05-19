from rest_framework import serializers
from .models import Video_category, Video_course, VideoCourse, Short_video
from authentication.serializer import UserSerializer, UserLikeSerializer
class Video_category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Video_category
        fields = "__all__"


class Video_course_serializer(serializers.ModelSerializer):
    class Meta:
        model = Video_course
        fields = ("course_name",)


class VideoCourseSerializer(serializers.ModelSerializer):
    category = Video_category_serializer()
    course = Video_course_serializer()
    likes = UserLikeSerializer(many=True)
    class Meta:
        model = VideoCourse
        fields = "__all__"



class short_video_serializer(serializers.ModelSerializer):
    shorts_author = UserSerializer()
    class Meta:
        model = Short_video
        fields = "__all__"
