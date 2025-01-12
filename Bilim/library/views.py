from django.shortcuts import render

def library(request):
    return render(request, "core/library.html")


def book_details(request):
    return render(request, "core/book_details.html")