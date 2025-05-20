from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.hashers import make_password
from .models import User, User_abilities, subscription
from django.contrib.auth.decorators import login_required
from videos.models import VideoCourse, Video_category, Short_video
from .tasks import send_custom_email
from django.conf import settings
from django.utils.html import format_html

#API views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer, SubscriptionSerializer, UserAbilitiesSerializer


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
        shorts = Short_video.objects.filter(shorts_accepted=False)
        courses = Video_category.objects.all()
        context = {
            "all_videos": videos,
            "courses":courses,
            "shorts":shorts
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
            popular_videos = Short_video.objects.filter(shorts_author=request.user)
            context = {
                "courses":courses,
                "popular_videos": popular_videos
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
    

@login_required
def admin_video_shorts(request, id):
    if request.method == "GET":
        courses = Video_category.objects.all()
        video = Short_video.objects.get(id=id)
        context = {
            "video": video,
            "courses":courses
        }
        return render(request, "core/video_page_for_admin_shorts.html", context)
    
def accept_video(request, id):
    if request.method == "GET":
        video = VideoCourse.objects.get(id=id)
        try:
            html_message = format_html(f"""
                <div style="text-align: center; font-family: Arial, sans-serif; padding: 20px;">
                    <img src="https://kepilli.com.tm/static/core/img/logo.svg" alt="Accepted" style="width: 100px;">
                    <h2 style="color: #4CAF50;">Ваше видео успешно принято!</h2>
                    <h2 style="color: #4CAF50;">Siziň widoeňyz üstünlikli goýuldy!</h2>
                    <p style="font-size: 16px; color: #333;">С уважением, команда <strong>Bilim!</strong></p>
                    <p style="font-size: 16px; color: #333;">Hormatlamak bilen <strong>Bilim</strong> komandasy!</p>
                    <hr style="margin: 20px 0;">
                    <h3>📹 Видео: <strong>{video.title}</strong></h3>
                    <h3>📹 Wideo: <strong>{video.title}</strong></h3>
                    <p>📚 Курс: {video.course.course_name}</p>
                    <p>📚 Kurs: {video.course.course_name}</p>
                    <p>📂 Категория: {video.category.category_name}</p>
                    <p>📂 Bölüm: {video.category.category_name}</p>
                    <p>✨ Теперь ваше видео доступно для студентов!</p>
                    <p>✨ Indi siziň wideoňyz talyplar üçin elýeterdir!</p>
                </div>
            """)

            send_custom_email.delay([video.author.email], "BILIM EDUCATION", html_message)
            video.accepted = True
            video.save()
            return redirect("auth:admin_page")
        except Exception as e:
            print("Failed to send email:", e)
            return redirect("auth:admin_page")
        

   
def accept_video_shorts(request, id):
    if request.method == "GET":
        video = Short_video.objects.get(id=id)
        try:
            html_message = format_html(f"""
                <div style="text-align: center; font-family: Arial, sans-serif; padding: 20px;">
                    <img src="https://kepilli.com.tm/static/core/img/logo.svg" alt="Accepted" style="width: 100px;">
                    <h2 style="color: #4CAF50;">Ваше видео успешно принято!</h2>
                    <h2 style="color: #4CAF50;">Siziň widoeňyz üstünlikli goýuldy!</h2>
                    <p style="font-size: 16px; color: #333;">С уважением, команда <strong>Bilim!</strong></p>
                    <p style="font-size: 16px; color: #333;">Hormatlamak bilen <strong>Bilim</strong> komandasy!</p>
                    <hr style="margin: 20px 0;">
                    <h3>📹 Видео: <strong>{video.shorts_title}</strong></h3>
                    <h3>📹 Wideo: <strong>{video.shorts_title}</strong></h3>
                    <p>✨ Теперь ваше видео доступно для студентов!</p>
                    <p>✨ Indi siziň wideoňyz talyplar üçin elýeterdir!</p>
                </div>
            """)

            send_custom_email.delay([video.shorts_author.email], "BILIM EDUCATION", html_message)
            video.shorts_accepted = True
            video.save()
            return redirect("auth:admin_page")
        except Exception as e:
            print("Failed to send email:", e)
            return redirect("auth:admin_page")



def decline_video(request, id):
    if request.method == "GET":
        video = VideoCourse.objects.get(id=id)
        try:
            html_message = format_html(f"""
                <div style="text-align: center; font-family: Arial, sans-serif; padding: 20px;">
                    <img src="https://kepilli.com.tm/static/core/img/logo.svg" alt="Rejected" style="width: 100px;">
                    <h2 style="color: #E53935;">К сожалению, ваше видео не принято!</h2>
                    <h2 style="color: #E53935;">Gynansakda siziň wideoňyz kabul edilmedi!</h2>
                    <p style="font-size: 16px; color: #333;">Пожалуйста, проверьте правильность введенных данных.</p>
                    <p style="font-size: 16px; color: #333;">Haýyş, girizen maglumatlaryňyzy dogry giriziň!</p>
                    <hr style="margin: 20px 0;">
                    <h3>📹 Видео: <strong>{video.title}</strong></h3>
                    <h3>📹 Wideo: <strong>{video.title}</strong></h3>
                    <p>📚 Курс: {video.course.course_name}</p>
                    <p>📚 Kurs: {video.course.course_name}</p>
                    <p>📂 Категория: {video.category.category_name}</p>
                    <p>📂 Bölüm: {video.category.category_name}</p>
                    <p>❌ Попробуйте снова загрузить видео с исправленными данными.</p>
                    <p>❌ Wideony gaýtaldan dogry maglumatlar bilen ýüklemegiňizi haýyş edýaris!.</p>
                    <p>С уважением, команда <strong>Bilim!</strong></p>
                    <p>Hormatlamak bilen <strong>Bilim</strong> komandasy!</p>
                </div>
            """)

            send_custom_email.delay([video.author.email], "BILIM EDUCATION", html_message)
            video.delete()
            return redirect("auth:admin_page")
        except Exception as e:
            print("Failed to send email:", e)
            return redirect("auth:admin_page")




def decline_video_shorts(request, id):
    if request.method == "GET":
        video = Short_video.objects.get(id=id)
        try:
            html_message = format_html(f"""
                <div style="text-align: center; font-family: Arial, sans-serif; padding: 20px;">
                    <img src="https://kepilli.com.tm/static/core/img/logo.svg" alt="Rejected" style="width: 100px;">
                    <h2 style="color: #E53935;">К сожалению, ваше видео не принято!</h2>
                    <h2 style="color: #E53935;">Gynansakda siziň wideoňyz kabul edilmedi!</h2>
                    <p style="font-size: 16px; color: #333;">Пожалуйста, проверьте правильность введенных данных.</p>
                    <p style="font-size: 16px; color: #333;">Haýyş, girizen maglumatlaryňyzy dogry giriziň!</p>
                    <hr style="margin: 20px 0;">
                    <h3>📹 Видео: <strong>{video.shorts_title}</strong></h3>
                    <h3>📹 Wideo: <strong>{video.shorts_title}</strong></h3>
                    <p>❌ Попробуйте снова загрузить видео с исправленными данными.</p>
                    <p>❌ Wideony gaýtaldan dogry maglumatlar bilen ýüklemegiňizi haýyş edýaris!.</p>
                    <p>С уважением, команда <strong>Bilim!</strong></p>
                    <p>Hormatlamak bilen <strong>Bilim</strong> komandasy!</p>
                </div>
            """)

            send_custom_email.delay([video.shorts_author.email], "BILIM EDUCATION", html_message)
            video.delete()
            return redirect("auth:admin_page")
        except Exception as e:
            print("Failed to send email:", e)
            return redirect("auth:admin_page")


@login_required
@api_view(["GET"])
def api_user_get(request):
    users = User.objects.all()
    serialized_data = UserSerializer(users, many=True).data
    return Response(serialized_data)


@login_required
@api_view(["POST"])
def api_user_create(request):
    data = request.data 
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

@login_required
@api_view(["GET"])
def api_subscription_get(request):
    subscriptions = subscription.objects.all()
    serialized_data = SubscriptionSerializer(subscriptions, many=True).data
    return Response(serialized_data)


@login_required
@api_view(["POST"])
def api_subscription_post(request):
    data = request.data
    serializer = SubscriptionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED )
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

@login_required
@api_view(["GET"])
def api_user_abilities_get(request):
    user_abilities = User_abilities.objects.all()
    serialized_data = UserAbilitiesSerializer(user_abilities, many=True).data
    return Response(serialized_data)


