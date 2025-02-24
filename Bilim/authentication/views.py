from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.hashers import make_password
from .models import User, User_abilities
from django.contrib.auth.decorators import login_required
from videos.models import VideoCourse, Video_category
from django.core.mail import send_mail
from django.conf import settings

#ready function
def login(request):
    if request.method == "GET":
        return render(request, "core/login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("core:index")
        else:
            return redirect("core:error")



#ready function
def sign_up(request):
    if request.method == "GET":
        return render(request, "core/sign_up.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password = make_password(password)
        email = request.POST.get("email")
        option = request.POST.get("option")
        if option == "student":
            user = User(username=username, email=email, password=password, is_student=True)
        if option == "teacher":
            user = User(username=username, email=email, password=password, is_teacher=True)
        try:
            user.save()
            return redirect("core:success")
        except Exception as e:
            return redirect("core:error")

@login_required
def payment(request):
    if request.method == "GET":
        courses = Video_category.objects.all()
        context = {
            "courses":courses
        }
        return render(request, "core/payment.html", context)


@login_required
def admin_page(request):
    if request.method == 'GET':
        videos = VideoCourse.objects.filter(accepted=False)
        courses = Video_category.objects.all()
        context = {
            "all_videos": videos,
            "courses":courses
        }
        return render(request, "core/admin.html", context)

#ready function
@login_required
def logout_user(request):
    logout(request)
    return redirect("auth:login")


#ready function
@login_required
def profile(request):
    if request.method == "GET":
        if request.user.is_student:
            courses = Video_category.objects.all()
            context = {
                "courses":courses
            }
            return render(request, "core/profile.html", context)


#ready function
@login_required
def edit_profile(request):
    if request.method == "GET":
        abilities = User_abilities.objects.all()
        courses = VideoCourse.objects.all()
        context = {
            "abilities": abilities,
            "courses":courses
        }
        return render(request, "core/profile_edit.html", context)
    if request.method == 'POST':
        username = request.POST.get("username")
        job = request.POST.get("job")
        about_me = request.POST.get("about_me")
        goals = request.POST.get("goals")
        selected_abilities = request.POST.get("selected_abilities")
        selected_abilities = selected_abilities.split(",")
        user_image = request.FILES.get("profile_image")
        print(user_image)
        for i in range(len(selected_abilities)):
            selected_abilities[i] = selected_abilities[i].title().strip()
        abilities = User_abilities.objects.filter(name__in=selected_abilities)

        user = User.objects.get(username=request.user.username)

        user.username = username.strip()
        user.job = job.strip()
        user.about_me = about_me.strip()
        user.about_my_goals = goals.strip()
        user.user_abilities.set(abilities)
        if not (user_image == None):
            user.user_avatar = user_image
        else:
            user.user_avatar = user.user_avatar
        try:
            user.save()
            return redirect("auth:profile")
        except Exception as e:
            print("Error: {e}")
            return render(request, "core/error.html")


@login_required
def admin_video(request, id):
    if request.method == "GET":
        courses = Video_category.objects.all()
        video = VideoCourse.objects.get(id=id)
        context = {
            "video": video,
            "courses":courses
        }
        return render(request, "core/video_page_for_admin.html", context)
    

def accept_video(request, id):
    if request.method == "GET":
        video = VideoCourse.objects.get(id=id)
        try:
            send_custom_email(video.author.email,"BILIM EDUCATION", "Ваше видео успешно принято!\nС уважением команда Bilim!\nSiziň goýan wideoňyz kabul edildi!\nHormatlamak bilen Bilim komandasy!")
            video.accepted = True
            video.save()
            return redirect("auth:admin_page")
        except Exception as e:
            print("Failed to save")
            return redirect("auth:admin_page")
        

    
def decline_video(request, id):
    if request.method == "GET":
        video = VideoCourse.objects.get(id=id)
        try:
            send_custom_email(video.author.email,"BILIM EDUCATION", "К сожалению ваше видео не принято! Попробуйте указать заданные поля правильные значения!\nС уважением команда Bilim!\nSiziň goýan wideoňyz kabul edilmedi! Görkezilen öýjüklere dogry maglumat girizmegiňi haýyş edýäris!\nHormatlamak bilen Bilim komandasy!")
            video.delete()
            return redirect("auth:admin_page")
        except Exception as e:
            print("Failed to delete")
            return redirect("auth:admin_page")




def send_custom_email(toemail, subject, message):
    try:
        send_mail(
            subject, 
            message,
            settings.EMAIL_HOST_USER,   
            [toemail],
            fail_silently=True
        )
        print("Successfully send")
    except Exception as e:
        print(f"Failed to send email: {e}")