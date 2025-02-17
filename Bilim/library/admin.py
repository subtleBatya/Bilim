from django.contrib import admin
from .models import Book, BookCategory


class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "views", "added_date")
    list_filter = ("name", "category", "views", "added_date")

admin.site.register(Book, BookAdmin)
admin.site.register(BookCategory)