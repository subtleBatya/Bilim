from django.shortcuts import render

def library(request):
    return render(request, "core/library.html")