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
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import get_object_or_404
import datetime
from django.utils import timezone
# Create your views here.
@login_required
def create_chat(request):
    context = {
    "students": request.user.followers.all()
    }
    return render(request, "core/video_chat/create_chat.html", context)



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



        return JsonResponse({"status": "ok"})

    return JsonResponse({"error": "Invalid request"}, status=400)





@login_required
def room(request, room_name):
    # Get or create the group chat first (shared by both student and teacher)
    group_chat, created = Group_chat.objects.get_or_create(group_name=room_name)

    if request.user.is_student: 
        lesson = get_object_or_404(New_lesson, lesson_name=room_name)
        
        if request.user not in lesson.accept_granted_students.all():
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
    
    return JsonResponse({'token': token, 'uid': uid, "username": username}, safe=False)

