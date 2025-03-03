from django.shortcuts import render, redirect
from authentication.models import User
from django.contrib.auth.decorators import login_required
from videos.models import VideoCourse, Video_category
# Create your views here.
@login_required
def all_users(request):
    if request.user.is_student or request.user.is_teacher:
        if request.method == "GET":
            users = User.objects.all()
            courses = Video_category.objects.all()
            context = {
                "users":users,
                "courses":courses
            }
            return render(request, "core/bilim_users.html", context)


@login_required
def exact_user(request, id):
    if request.method == "GET":
        if request.user.is_student or request.user.is_teacher:
            user = User.objects.get(id=id)
            user_videos = VideoCourse.objects.filter(author=user)
            courses = Video_category.objects.all()
            subscribers = user.followers.all()
            subscribe_videos = VideoCourse.objects.filter(author__in=subscribers)
            context = {
                "user": user,
                "user_videos": user_videos,
                "courses":courses,
                "subscribed_videos":subscribe_videos
            }
            return render(request, "core/bilim_exact_user.html", context)
        

@login_required
def follow(request, id):
    user = User.objects.get(id=id)
    following_user = request.user
    if following_user in user.followers.all():
        user.followers.remove(following_user)
        followed = False
    else:
        user.followers.add(following_user)
        followed = True
        
    return redirect("users:all_users")