from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book, BookCategory
from django.shortcuts import get_object_or_404
from videos.models import Video_category
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from django.template.loader import render_to_string

#API views
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializer import BookSerializer
from rest_framework import status 

@login_required
def library(request):
    book_name = request.GET.get("book_name")
    category_name = request.GET.get("category")

    courses = Video_category.objects.all()
    categories = BookCategory.objects.all()
    books = Book.objects.all()

    if book_name and category_name:
        books = books.filter(name__icontains=book_name, category__category_name=category_name)
    elif book_name:
        books = books.filter(name__icontains=book_name)
    elif category_name:
        books = books.filter(category__category_name=category_name)

    paginator = Paginator(books, 9)
    page_number = int(request.GET.get("page", 1))

    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_obj = []

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        html = render_to_string("core/partials/book_cards.html", {"books": page_obj}, request=request)
        return JsonResponse({
            "html": html,
            "has_next": page_obj.has_next() if hasattr(page_obj, 'has_next') else False
        })

    context = {
        "books": page_obj,
        "categories": categories,
        "book_name": book_name,
        "category_name": category_name,
        "courses": courses
    }
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
    

@login_required
@api_view(["GET"])
def api_books_get(request):
    books = Book.objects.all()
    serialized_data = BookSerializer(books, many=True).data
    return Response(serialized_data)