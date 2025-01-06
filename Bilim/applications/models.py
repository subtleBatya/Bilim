from django.db import models

# Create your models here.
class Application(models.Model):
    application_owner = models.CharField(max_length=255)
    application_text = models.TextField()


    def __str__(self):
        return self.application_owner