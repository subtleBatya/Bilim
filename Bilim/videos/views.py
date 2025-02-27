from django.shortcuts import render
from .models import VideoCourse, Video_course as category_courses, Video_category, Short_video
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from authentication.models import User, UserRecentVideo
import random
# Create your views here.
@login_required
def all_courses(request, id):
    if request.method == "GET":
        courses = Video_category.objects.all()
        main_category = Video_category.objects.get(id=id)
        category_course = category_courses.objects.filter(related_category__category_name=main_category.category_name)
        course_category = request.GET.get("category")
        video_name = request.GET.get("video_name")
        all_videos = VideoCourse.objects.filter(accepted=True, category__category_name=main_category.category_name)
        if course_category and video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, title__icontains=video_name, course__course_name=course_category, category__category_name=main_category.category_name)
        if course_category and not video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, course__course_name=course_category, category__category_name=main_category.category_name)
        if not course_category and video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, title__icontains=video_name, category__category_name=main_category.category_name)
        context = {
            "all_videos": all_videos,
            "category_courses": category_course,
            "course_name":course_category,
            "video_name": video_name,
            "main_cat_name": main_category.category_name,
            "courses":courses
        }
        return render(request, "core/all_courses.html", context)

@login_required
def video_of_course(request, id):
    if request.method == "GET":
        courses = Video_category.objects.all()
        video = VideoCourse.objects.get(id=id)
        user = User.objects.get(username=request.user.username)
        
        UserRecentVideo.objects.filter(user=user, video=video).delete()

        UserRecentVideo.objects.create(user=user, video=video)
        recent_videos = UserRecentVideo.objects.filter(user=user).order_by("-timestamp")
        if recent_videos.count() > 20:
            to_delete = recent_videos[20:]
            UserRecentVideo.objects.filter(id__in=[rv.id for rv in to_delete]).delete()

        video.views += 1
        video.save()
        popular_videos = VideoCourse.objects.all().exclude(author=request.user).order_by("?")[:20]
        context = {
            "video": video,
            "courses":courses,
            "popular_videos":popular_videos
        }
        return render(request, "core/video_page.html", context)

@login_required
def create_shorts(request):
    if request.method == "GET":
        courses = Video_category.objects.all()
        context = {
            "courses":courses
        }
        return render(request, "core/create_shorts.html", context)
    if request.method == "POST":
        video = request.FILES.get("video")
        video_title = request.POST.get("video_title")
        video_description = request.POST.get("video_description")
        poster = request.FILES.get("poster")

        lesson = Short_video(
                shorts_video=video,
                shorts_title=video_title,
                shorts_description=video_description,
                shorts_poster=poster,
                shorts_author=request.user
            )
        try:
            lesson.save()
            return JsonResponse({"message": "Video uploaded successfully!"}, status=200)
        except Exception as e:
            return JsonResponse({"error": f"Error saving video: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@login_required
def like_video(request, video_id):
    video = get_object_or_404(VideoCourse, id=video_id)
    user = request.user

    if user in video.likes.all():
        video.likes.remove(user)  # Unlike
        liked = False
    else:
        video.likes.add(user)  # Like
        liked = True

    return JsonResponse({"liked": liked, "like_count": video.likes.count()})



def shorts(request):
    if request.method == "GET":
        user = User.objects.get(username=request.user.username)
        videos = Short_video.objects.filter(shorts_accepted=True).order_by("?")  
        paginator = Paginator(videos, 10) 
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        return render(request, 'core/shorts/shorts.html', {
            'page_obj': page_obj,
            'has_next': page_obj.has_next(),  # Check if more pages are available
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
        })
