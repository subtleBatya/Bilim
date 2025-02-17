from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book, BookCategory
from django.shortcuts import get_object_or_404
@login_required
def library(request):
    if request.method == "GET":
        book_name = request.GET.get("book_name")
        category_name = request.GET.get("category")
        
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
                "category_name": category_name
            }
        print(categories)
        return render(request, "core/library.html", context)
        


@login_required
def book_details(request, id):
    books = Book.objects.get(id=id)
    books.views += 1
    books.save()
    context = {
        "book": books
    }
    return render(request, "core/book_details.html", context)