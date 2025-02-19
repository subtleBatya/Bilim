from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    return render(request, "core/index.html")

@login_required
def success(request):
    return render(request, "core/success.html")

@login_required
def error(request):
    return render(request, "core/error.html")