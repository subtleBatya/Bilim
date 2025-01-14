from django.shortcuts import render

def login(request):
    return render(request, "core/login.html")



def sign_up(request):
    return render(request, "core/sign_up.html")


def payment(request):
    return render(request, "core/payment.html")




def teacher_profile(request):
    return render(request, "core/teacher_profile.html")



def teacher_video_create(request):
    return render(request, "core/teacher_create_video.html")