from django.shortcuts import render
from videos.models import Video_category
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def all_users(request):
    if request.user.is_staff:
        courses = Video_category.objects.all()
        context = {
            "courses":courses
        }
        return render(request, "core/bilim_users.html", context)



def exact_user(request):
    if request.user.is_staff:
        courses = Video_category.objects.all()
        context = {
            "courses":courses
        }
        return render(request, "core/bilim_exact_user.html", context)