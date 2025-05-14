from .models import Book, BookCategory
from rest_framework import serializers


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    category = BookCategorySerializer(BookCategory, read_only=True)
    class Meta:
        model = Book
        fields = "__all__"


