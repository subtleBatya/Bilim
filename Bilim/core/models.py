from django.db import models
from auth.models import Teacher


class VideoCourse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_courses = models.ManyToManyField(VideoCourse, related_name='collections')
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='collections')

    def __str__(self):
        return self.name
