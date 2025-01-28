from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class User(AbstractUser):
    telephone_number = models.CharField(max_length=255, blank=True, null=True)
    user_avatar = models.ImageField(upload_to="user/images/", blank=True, null=True)
    #recent_seen_video = models.ManyToManyField()
    is_student = models.BooleanField(default=False, blank=True)
    is_teacher = models.BooleanField(default=False, blank=True)
    about_me = models.TextField(blank=True, null=True)
    about_my_goals = models.TextField(blank=True, null=True)
    about_me_shorter = models.ManyToManyField("About_user", blank=True)
    user_abilities = models.ManyToManyField("User_abilities", blank=True)

    
    def __str__(self):
        return self.username
    

class subscription(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_start_date = models.DateTimeField(blank=True, null=True)
    subscription_end_date = models.DateTimeField(blank=True, null=True)


    def is_active(self):
        return self.subscription_end_date < timezone.now()
    
    def __str__(self):
        return self.username
    

class About_user(models.Model):
    icon = models.ImageField(upload_to="icons/about_me/")
    text = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'About User'
        verbose_name_plural = 'About Users'

    def __str__(self):
        return f"{self.text}"
    


class User_abilities(models.Model):
    name = models.CharField(max_length=255)
    ability_icon = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'User Ability'
        verbose_name_plural = 'User Abilities'

    def __str__(self):
        return self.name