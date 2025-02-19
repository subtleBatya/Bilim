from django.db import models




class Video_category(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Main video category'
        verbose_name_plural = 'Main video categories'

    def __str__(self):
        return self.category_name


class Video_course(models.Model):
    course_name = models.CharField(max_length=255)
    related_category = models.ForeignKey(Video_category, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Course category'
        verbose_name_plural = 'Course categories'

    def __str__(self):
        return self.course_name


class VideoCourse(models.Model):
    category = models.ForeignKey(Video_category, on_delete=models.CASCADE)
    course = models.ForeignKey(Video_course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to="posters/")
    video = models.FileField(upload_to='videos/')
    views = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField("authentication.User", related_name="Liked_users", blank=True)
    author = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name="Author_of_video", blank=True)
    added_date = models.DateTimeField(auto_now_add=True, blank=True)
    accepted = models.BooleanField(default=False)

    def get_likes_count(self):
        from authentication.models import User
        return self.likes.count()


    def __str__(self):
        return self.title

