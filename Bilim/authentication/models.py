from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    telephone_number = models.CharField(max_length=255, blank=True, null=True)
    user_avatar = models.ImageField(upload_to="user/images/", blank=True, null=True)

    def __str__(self):
        return self.username
    
class Student(User):
    subscription_start_date = models.DateTimeField(blank=True, null=True)
    subscription_end_date = models.DateTimeField(blank=True, null=True)
    recent_seen_video = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

class Teacher(User):
    videos = models.TextField(blank=True, null=True)  # should think about dis field, can use Json or foreignkey idk, should think more

    def __str__(self):
        return self.username