from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from videos.models import Video_category, VideoCourse as Videos
from .models import Scientist
from django.db.models import Count

#API view
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializer import ScientistSerializer
# Create your views here.
@login_required
def index(request):
    courses = Video_category.objects.all()
    videos = Videos.objects.annotate(likes_count=Count("likes")).order_by("-likes_count", "-views")[:12]
    scientists = []
    for scientist in Scientist.objects.all().order_by("?"):
        if scientist in scientists:
            pass
        else:
            if len(scientists) == 3:
                break
            scientists.append(scientist)
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



def error_404_view(request, exception):
    return render(request, "core/404.html", status=404)


def error_500_view(request):
    return render(request, "core/500.html", status=500)


@api_view(["GET"])
def api_get_scientist(request):
    scientists = Scientist.objects.all()
    data = ScientistSerializer(scientists, many=True).data 
    return Response(data)