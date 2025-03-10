from django.shortcuts import render, redirect
from authentication.models import User, User_abilities
from videos.models import Video_course, Video_category, VideoCourse as VideoLesson
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def teacher_profile(request):
    if request.user.is_teacher:
        courses = Video_category.objects.all()
        context = {
            "courses":courses
        }
        return render(request, "core/teacher_profile.html", context)

@login_required
def teacher_content(request):
    if request.method == "GET":
        if request.user.is_teacher:
            courses = Video_category.objects.all()
            teacher_lessons = VideoLesson.objects.filter(author=request.user)
            context = {
                "lessons": teacher_lessons,
                "courses":courses
            }
            return render(request, "core/teacher_content.html", context)
        
@login_required   
def teacher_content_delete(request, id):
    if request.method == "GET":
        if request.user.is_teacher:
            video = VideoLesson.objects.get(author=request.user, id=id)
            try:
                video.delete()
                return redirect("teacher:teacher_content")
            except Exception as e:
                print(f"Error: {e}")
                return redirect("core:error")
            
from django.http import JsonResponse

@login_required
def teacher_video_create(request):
    if request.method == "GET":
        if request.user.is_teacher:
            main_category = Video_category.objects.all()
            course_category = Video_course.objects.all()
            courses = Video_category.objects.all()
            context = {
                "main_category": main_category,
                "course_category": course_category,
                "courses":courses
            }
            return render(request, "core/teacher_create_video.html", context)

    elif request.method == "POST":
        if request.user.is_teacher:
            video = request.FILES.get("video")
            video_title = request.POST.get("video_title")
            main_category_name = request.POST.get("main_cat")
            course_category_name = request.POST.get("course_cat")
            video_description = request.POST.get("video_description")
            poster = request.FILES.get("poster")

            # Validate categories
            try:
                main_category = Video_category.objects.get(category_name=main_category_name)
                course_category = Video_course.objects.get(course_name=course_category_name)
            except Video_category.DoesNotExist:
                return JsonResponse({"error": "Invalid main category"}, status=400)
            except Video_course.DoesNotExist:
                return JsonResponse({"error": "Invalid course category"}, status=400)

            lesson = VideoLesson(
                video=video,
                title=video_title,
                category=main_category,
                course=course_category,
                description=video_description,
                poster=poster,
                author=request.user
            )
            try:
                lesson.save()
                return JsonResponse({"message": "Video uploaded successfully!"}, status=200)
            except Exception as e:
                return JsonResponse({"error": f"Error saving video: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)


@login_required
def teacher_edit(request):
    if request.method == "GET":
        if request.user.is_teacher:
            courses = Video_category.objects.all()
            abilities = User_abilities.objects.all()
            context ={
                "courses":courses,
                "abilities": abilities,
            }
            return render(request, "core/teacher_edit.html", context)
    if request.method == "POST":
        username = request.POST.get("username")
        job = request.POST.get("job")
        phone_number = request.POST.get("phone_number")
        image = request.FILES.get("profile_image")
        teacher = User.objects.get(username=request.user.username)
        selected_abilities = request.POST.get("selected_abilities")
        selected_abilities = selected_abilities.split(",")
        if not (image == None):
            teacher.user_avatar = image
        else:
            teacher.user_avatar = teacher.user_avatar
        for i in range(len(selected_abilities)):
            selected_abilities[i] = selected_abilities[i].title().strip()
        abilities = User_abilities.objects.filter(name__in=selected_abilities)
        teacher.username = username
        teacher.job = job
        teacher.telephone_number = phone_number
        teacher.user_abilities.set(abilities)
        try:
            teacher.save()
            return redirect("teacher:teacher_profile")
        except Exception as e:
            print(f"Error: {e}")
            return redirect("core:error")
        

@login_required
def see_own_video(request, id):
    my_video = VideoLesson.objects.get(author=request.user, id=id)
    context = {
        'video': my_video,
    }
    return render(request, "core/video_page_for_teachers.html", context)
