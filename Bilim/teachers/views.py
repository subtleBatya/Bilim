from django.shortcuts import render

# Create your views here.
def teacher_profile(request):
    return render(request, "core/teacher_profile.html")



def teacher_video_create(request):
    return render(request, "core/teacher_create_video.html")