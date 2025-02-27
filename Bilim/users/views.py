from django.shortcuts import render
from authentication.models import User
from django.contrib.auth.decorators import login_required
from videos.models import VideoCourse
# Create your views here.
@login_required
def all_users(request):
    if request.user.is_student or request.user.is_teacher:
        if request.method == "GET":
            users = User.objects.all()
            context = {
                "users":users
            }
            return render(request, "core/bilim_users.html", context)


@login_required
def exact_user(request, id):
    if request.method == "GET":
        if request.user.is_student or request.user.is_teacher:
            user = User.objects.get(id=id)
            user_videos = VideoCourse.objects.filter(author=user)
            
            context = {
                "user": user,
                "user_videos": user_videos
            }
            return render(request, "core/bilim_exact_user.html", context)