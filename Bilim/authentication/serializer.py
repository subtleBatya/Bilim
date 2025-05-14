from rest_framework import serializers
from .models import *
from videos.models import VideoCourse

class UserAbilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_abilities
        fields = "__all__"


class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class VideoCourseSerializer(serializers.ModelSerializer):
    likes = UserLikeSerializer(many=True, read_only=True)
    class Meta:
        model = VideoCourse
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_abilities = UserAbilitiesSerializer(many=True, read_only=True)
    recent_seen_video = VideoCourseSerializer(many=True, read_only=True)
    followers = UserLikeSerializer(many=True, read_only=True)
    followed = UserLikeSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    username = UserLikeSerializer(many=False, read_only=True)
    class Meta:
        model = subscription
        fields = "__all__"


