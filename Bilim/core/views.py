from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from videos.models import Video_category 
# Create your views here.
@login_required
def index(request):
    courses = Video_category.objects.all()
    context = {
        "courses":courses
    }
    return render(request, "core/index.html", context)

@login_required
def success(request):
    return render(request, "core/success.html")

@login_required
def error(request):
    return render(request, "core/error.html")