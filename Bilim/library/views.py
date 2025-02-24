from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book, BookCategory
from django.shortcuts import get_object_or_404
from videos.models import Video_category
@login_required
def library(request):
    if request.method == "GET":
        book_name = request.GET.get("book_name")
        category_name = request.GET.get("category")
        courses = Video_category.objects.all()
        books = Book.objects.all()
        categories = BookCategory.objects.all()
    
        if book_name and category_name:
            books = Book.objects.filter(name__icontains=book_name, category__category_name=category_name)
        elif book_name and category_name is not None:
            books = Book.objects.filter(name__icontains=book_name)
        elif book_name is not None and category_name:
            books = Book.objects.filter(category__category_name=category_name)

        context = {
                "books": books,
                "categories": categories,
                "book_name":book_name,
                "category_name": category_name,
                "courses":courses
            }
        print(categories)
        return render(request, "core/library.html", context)
        


@login_required
def book_details(request, id):
    if request.method == "GET":
        books = Book.objects.get(id=id)
        courses = Video_category.objects.all()
        books.views += 1
        books.save()
        context = {
            "book": books,
            "courses": courses
        }
        return render(request, "core/book_details.html", context)