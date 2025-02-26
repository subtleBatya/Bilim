from django.db import models

class Scientist(models.Model):
    scientist_name = models.CharField(max_length=30)
    scientist_image = models.ImageField(upload_to="scientist/images/")
    scientist_text = models.CharField(max_length=255)


    def __str__(self):
        return self.scientist_name