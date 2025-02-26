from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from videos.models import Video_category, VideoCourse as Videos
# Create your views here.
@login_required
def index(request):
    courses = Video_category.objects.all()
    videos = Videos.objects.all().order_by("-likes")[:12]
    context = {
        "courses":courses,
        "popular_videos": videos
    }
    return render(request, "core/index.html", context)

@login_required
def success(request):
    return render(request, "core/success.html")

@login_required
def error(request):
    return render(request, "core/error.html")