from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username

class Student(BaseUser):
    subscription_start_date = models.DateTimeField(blank=True, null=True)
    subscription_end_date = models.DateTimeField(blank=True, null=True)
    recent_seen_video = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

class Teacher(BaseUser):
    videos = models.TextField(blank=True, null=True)  # should think about dis field, can use Json or foreignkey idk, should think more

    def __str__(self):
        return self.username
