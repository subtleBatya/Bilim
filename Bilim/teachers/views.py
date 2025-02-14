from django.shortcuts import render, redirect
from authentication.models import User

# Create your views here.
def teacher_profile(request):
    return render(request, "core/teacher_profile.html")


def teacher_content(request):
    return render(request, "core/teacher_content.html")



def teacher_video_create(request):
    return render(request, "core/teacher_create_video.html")


def teacher_edit(request):
    if request.method == "GET":
        if request.user.is_teacher:
            return render(request, "core/teacher_edit.html")
    if request.method == "POST":
        username = request.POST.get("username")
        job = request.POST.get("job")
        phone_number = request.POST.get("phone_number")
        image = request.FILES.get("profile_image")
        teacher = User.objects.get(username=request.user.username)
        if not (image == None):
            teacher.user_avatar = image
        else:
            teacher.user_avatar = teacher.user_avatar
        
        teacher.username = username
        teacher.job = job
        teacher.telephone_number = phone_number
        try:
            teacher.save()
            return redirect("teacher:teacher_profile")
        except Exception as e:
            print(f"Error: {e}")
            return redirect("core:error")
