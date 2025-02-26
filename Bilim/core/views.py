from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from videos.models import Video_category, VideoCourse as Videos
from .models import Scientist
import random
# Create your views here.
@login_required
def index(request):
    courses = Video_category.objects.all()
    videos = Videos.objects.all().order_by("-likes")[:12]
    scientists = []
    for scientist in Scientist.objects.all().order_by("?"):
        if scientist in scientists:
            pass
        else:
            if len(scientists) == 3:
                break
            scientists.append(scientist)
    print(scientists)
    context = {
        "courses":courses,
        "popular_videos": videos,
        "scientists": scientists
    }
    return render(request, "core/index.html", context)

@login_required
def success(request):
    return render(request, "core/success.html")

@login_required
def error(request):
    return render(request, "core/error.html")