from django.db import models
from authentication.models import User
# Create your models here.
class Group_chat(models.Model):
    group_name = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User, blank=True)
    is_private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.group_name

class ChatMessage(models.Model):
    room_name = models.ForeignKey(Group_chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.send_time}, {self.sender.username}, {self.message}'
    


class New_lesson(models.Model):
    lesson_name = models.CharField(max_length=255, unique=True)
    teacher_name = models.CharField(max_length=255, blank=True)
    accept_granted_students = models.ManyToManyField(User, blank=True)


    def __str__(self):
        return self.lesson_name