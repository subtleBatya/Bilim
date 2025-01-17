from django.db import models
from authentication.models import User
# Create your models here.
class Application(models.Model):
    application_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    application_text = models.TextField()


    def __str__(self):
        return self.application_owner.username