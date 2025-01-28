from django.db import models
from videos.models import Video_course

# Create your models here.
class Question(models.Model):
    related_course = models.ForeignKey(Video_course, on_delete=models.CASCADE)
    question = models.TextField()


    def __str__(self):
        return self.question
    


class Answer(models.Model):
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)


    def __str__(self):
        return self.answer
