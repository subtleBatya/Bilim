from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")


def success(request):
    return render(request, "core/success.html")


def error(request):
    return render(request, "core/error.html")