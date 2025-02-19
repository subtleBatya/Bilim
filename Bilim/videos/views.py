from django.shortcuts import render
from .models import VideoCourse, Video_course as category_courses
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def technical_courses(request):
    if request.method == "GET":
        category_course = category_courses.objects.filter(related_category__category_name="Technical")
        course_category = request.GET.get("category")
        video_name = request.GET.get("video_name")
        all_videos = VideoCourse.objects.filter(accepted=True, category__category_name="Technical")
        if course_category and video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, title__icontains=video_name, course__course_name=course_category, category__category_name="Technical")
        if course_category and not video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, course__course_name=course_category, category__category_name="Technical")
        if not course_category and video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, title__icontains=video_name, category__category_name="Technical")
        context = {
            "all_videos": all_videos,
            "category_courses": category_course,
            "course_name":course_category,
            "video_name": video_name
        }
        return render(request, "core/technical-courses.html", context)
    
@login_required
def natural_courses(request):
    if request.method == "GET":
        category_course = category_courses.objects.filter(related_category__category_name="Natural")
        course_category = request.GET.get("category")
        video_name = request.GET.get("video_name")
        all_videos = VideoCourse.objects.filter(accepted=True, category__category_name="Natural" )
        if course_category and video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, title__icontains=video_name, course__course_name=course_category, category__category_name="Natural")
        if course_category and not video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, course__course_name=course_category, category__category_name="Natural")
        if not course_category and video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, title__icontains=video_name, category__category_name="Natural")
        context = {
            "all_videos": all_videos,
            "category_courses": category_course,
            "course_name":course_category,
            "video_name": video_name
        }
        return render(request, "core/natural-courses.html", context)


@login_required
def humanitar_courses(request):
    if request.method == "GET":
        category_course = category_courses.objects.filter(related_category__category_name="Humanitar")
        course_category = request.GET.get("category")
        video_name = request.GET.get("video_name")
        all_videos = VideoCourse.objects.filter(accepted=True, category__category_name="Humanitar" )
        if course_category and video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, title__icontains=video_name, course__course_name=course_category, category__category_name="Humanitar")
        if course_category and not video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, course__course_name=course_category, category__category_name="Humanitar")
        if not course_category and video_name:
            all_videos = VideoCourse.objects.filter(accepted=True, title__icontains=video_name, category__category_name="Humanitar")
        context = {
            "all_videos": all_videos,
            "category_courses": category_course,
            "course_name":course_category,
            "video_name": video_name
        }
        return render(request, "core/humanitar-courses.html", context)

@login_required
def video_of_course(request, id):
    if request.method == "GET":
        video = VideoCourse.objects.get(id=id)
        video.views += 1
        video.save()
        context = {
            "video": video
        }
        return render(request, "core/video_page.html", context)



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
    return render(request, "core/shorts.html")