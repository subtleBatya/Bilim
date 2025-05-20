from django.shortcuts import render, redirect
from authentication.models import User
from django.contrib.auth.decorators import login_required
from videos.models import VideoCourse, Video_category
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
from django.template.loader import render_to_string
# Create your views here.
@login_required
def all_users(request):
    if request.user.is_student or request.user.is_teacher and request.method == "GET" :
        users = User.objects.all()
        paginator = Paginator(users, 6) 
        page_number = request.GET.get("page", 1)

        try:
            page_obj = paginator.get_page(page_number)
        except EmptyPage:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"html": "", "has_next": False})
            page_obj = paginator.get_page(paginator.num_pages)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string("core/users_chunk.html", {"users": page_obj}, request=request)
            return JsonResponse({"html": html, "has_next": page_obj.has_next()})

        return render(request, "core/bilim_users.html", {
            "users": page_obj
        })


@login_required
def search_users(request):
    if request.method == "GET":
        username = request.GET.get("user_name")
        users = User.objects.filter(username__icontains=username)
        context = {
            "users": users,
            "user_name": username
        }
        return render(request, "core/bilim_users.html", context)



@login_required
def exact_user(request, id):
    if request.method == "GET":
        if request.user.is_student or request.user.is_teacher:
            user = User.objects.get(id=id)
            user_videos = VideoCourse.objects.filter(author=user)
            followed = user.followed.all()
            subscribe_videos = VideoCourse.objects.filter(author__in=followed)
            context = {
                "user": user,
                "user_videos": user_videos,
                "subscribed_videos":subscribe_videos
            }
            return render(request, "core/bilim_exact_user.html", context)
        

@login_required
def follow(request, id):
    user = get_object_or_404(User, id=id)
    following_user = request.user

    if following_user in user.followers.all():
        user.followers.remove(following_user)
        followed = False
    else:
        user.followers.add(following_user)
        followed = True

    if user in following_user.followed.all():
        following_user.followed.remove(user)
    else:
        following_user.followed.add(user)

    return JsonResponse({"followed": followed})
