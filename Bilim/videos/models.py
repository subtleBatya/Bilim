from django.db import models
from authentication.models import User



class Video_category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Video_course(models.Model):
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name


class VideoCourse(models.Model):
    category = models.ForeignKey(Video_category, on_delete=models.CASCADE)
    course = models.ForeignKey(Video_course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

