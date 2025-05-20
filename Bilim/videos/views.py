from django.shortcuts import render
from .models import VideoCourse, Video_course as category_courses, Video_category, Short_video
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from authentication.models import User, UserRecentVideo
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
#api views
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from .serializer import VideoCourseSerializer, short_video_serializer

# Create your views here.
@login_required
def all_courses(request, id):
    courses = Video_category.objects.all()
    main_category = Video_category.objects.get(id=id)
    category_course = category_courses.objects.filter(related_category=main_category)
    course_category = request.GET.get("category")
    video_name = request.GET.get("video_name")

    all_videos = VideoCourse.objects.filter(accepted=True, category=main_category)

    if course_category:
        all_videos = all_videos.filter(course__course_name=course_category)
    if video_name:
        all_videos = all_videos.filter(title__icontains=video_name)

    paginator = Paginator(all_videos, 10)  # Show 10 per page
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        return JsonResponse({'html': '', 'has_next': False})

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string("core/video_cards.html", {"all_videos": page_obj}, request=request)
        return JsonResponse({"html": html, "has_next": page_obj.has_next()})

    context = {
        "all_videos": page_obj,
        "category_courses": category_course,
        "course_name": course_category,
        "video_name": video_name,
        "main_cat_name": main_category.category_name,
        "courses": courses
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
        popular_videos = VideoCourse.objects.filter(accepted=True).exclude(author=request.user).order_by("?")[:20]
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



class ShortsFeed(View):
    @csrf_exempt
    def get(self, request):
        shorts = Short_video.objects.filter(shorts_accepted=True).order_by('-shorts_added_date')
        return render(request, 'core/shorts/shorts.html', {'shorts': shorts})

class IncrementShortView(View):
    @csrf_exempt
    def post(self, request, short_id):
        if request.method == "POST":
            short = get_object_or_404(Short_video, id=short_id)
            short.shorts_views += 1
            short.save()
            return JsonResponse({'status': 'success', 'views': short.shorts_views})


@login_required
def user_shorts(request, id):
    if request.method == "GET":
        videos = Short_video.objects.filter(shorts_author=request.user)
        paginator = Paginator(videos, 1) 
        page_number = request.GET.get('page', 10)
        page_obj = paginator.get_page(page_number)

        return render(request, 'core/shorts/shorts.html', {
            'page_obj': page_obj,
            'has_next': page_obj.has_next(),  # Check if more pages are available
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
        })


@api_view(["GET"])
def api_videocourses_get(request):
    videos = VideoCourse.objects.all()
    serialized_data = VideoCourseSerializer(videos, many=True).data
    return Response(serialized_data)


@api_view(["GET"])
def api_shorts_get(request):
    videos = Short_video.objects.all()
    serialized_data = short_video_serializer(videos, many=True).data
    return Response(serialized_data)