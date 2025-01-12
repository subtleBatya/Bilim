from django.shortcuts import render

# Create your views here.
def courses(request):
    return render(request, "core/courses.html")



def video_of_course(request):
    return render(request, "core/video_page.html")