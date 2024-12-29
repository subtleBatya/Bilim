from django.db import models

# Create your models here.
class BookCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'BookCategory'
        verbose_name_plural = 'BookCategories'


class Book(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)    
    description = models.TextField()
    views = models.IntegerField()
    book_file = models.FileField(upload_to="books/files")
    book_poster = models.FileField(upload_to="books/images")
    added_date = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.name 