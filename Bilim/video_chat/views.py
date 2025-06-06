from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder
import random
import time
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from authentication.models import User, subscription
import json
from django.http import HttpResponseForbidden, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
import datetime
from django.utils import timezone
from authentication.tasks import send_custom_email
# Create your views here.
@login_required
def create_chat(request):
    if request.user.is_teacher:
        context = {
        "students": request.user.followers.all()
        }
        return render(request, "core/video_chat/create_chat.html", context) 
    else:
        return HttpResponseNotAllowed("You are not allowed here! You are a student!")




@csrf_exempt
@login_required
def create_lesson(request):
    if request.method == "POST":
        print("POST request received")

        try:
            data = json.loads(request.body)
            print("Received data:", data)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        lesson_name = data.get("lesson_name")
        students = data.get("students", [])
        lesson = data.get('lesson')
        if not lesson_name:
            return JsonResponse({"error": "Missing lesson_name"}, status=400)

        print(f"Creating lesson: {lesson_name} for students: {students} Lesson name for students: {lesson}")

        lesson = New_lesson.objects.create(lesson_name_for_students=lesson, lesson_name=lesson_name,teacher_name=request.user.username)

        users = User.objects.filter(username__in=students)
        print("Matching users:", users)

        lesson.accept_granted_students.set(users)
        lesson.save()

        user_emails = [user.email for user in users if user.email]

        try:
            html_message = f"""
                    <div style="text-align: center; font-family: Arial, sans-serif; padding: 20px;">
                    <img src="https://kepilli.com.tm/static/core/img/logo.svg" alt="Accepted" style="width: 100px;">
                    <h2 style="color: #4CAF50;">Ваш учитель начал урок!</h2>
                    <h2 style="color: #4CAF50;">Mugallymyňyz sapagy başlady!</h2>
                    <h2 style="color: #4CAF50;">Зайдите на платформу и присоединитесь к уроку!</h2>
                    <h2 style="color: #4CAF50;">Platforma girip sapaga goşulyň!</h2>
                     <hr style="margin: 20px 0;">
                    <p>✨ Имя урока {lesson}.</p>
                    <p>✨ Sapagyň ady {lesson}.</p>
                    <p style="font-size: 16px; color: #333;">С уважением, команда <strong>Bilim!</strong></p>
                    <p style="font-size: 16px; color: #333;">Hormatlamak bilen <strong>Bilim</strong> komandasy!</p>
                </div>
"""         
            send_custom_email.delay(user_emails, "BILIM EDUCATION", html_message)
            print("Message send Successfully!")
        except Exception as e:
            print(f"Error: {e}")

        return JsonResponse({"status": "ok"})

    return JsonResponse({"error": "Invalid request"}, status=400)





@login_required
def room(request, room_name):
    # Get or create the group chat first (shared by both student and teacher)
    group_chat, created = Group_chat.objects.get_or_create(group_name=room_name)

    if request.user.is_student: 
        lesson = get_object_or_404(New_lesson, lesson_name=room_name)
        
        if request.user not in lesson.accept_granted_students.all() and request.user.subscription.is_active() :
            return HttpResponseForbidden("You don't have access to this lesson.")
        
        if lesson.data_created + datetime.timedelta(hours=2, minutes=30) < timezone.now():
            return HttpResponseForbidden("The lesson is expired")
        # Add student to group chat if not already in
        if request.user not in group_chat.users.all():
            group_chat.users.add(request.user)

        return render(request, "core/video_chat/room.html", {"room_name": room_name})

    elif request.user.is_teacher:
        # Add teacher to group chat if not already in
        if request.user not in group_chat.users.all():
            group_chat.users.add(request.user)

        return render(request, "core/video_chat/room.html", {"room_name": room_name})


    
    
@login_required
def available_lesson_for_student(request):
    if request.user.is_student:
        context = {
            "lessons": New_lesson.objects.filter(accept_granted_students=request.user)
        }
        return render(request, "core/video_chat/join_chat.html", context)
    


@csrf_exempt
def getToken(request):
    appId = "f761c240f7164bf293c1cb58eb3c5e8d"
    appCertificate = "f17e4fa36fc840bf98495ccef9d557da"
    channelName = request.GET.get("channel")
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    username = request.user.username
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    user = request.user
    user.uid = uid
    user.save()
    return JsonResponse({'token': token, 'uid': uid, "username": username}, safe=False)





@csrf_exempt
def get_username_by_uid(request):
    uid = request.GET.get("uid")
    try:
        user = User.objects.get(uid=uid)
        return JsonResponse({"username": user.username})
    except User.DoesNotExist:
        return JsonResponse({"username": "Unknown"})



