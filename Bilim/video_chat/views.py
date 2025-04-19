from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder
import random
import time
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@login_required
def create_chat(request):
    return render(request, "core/video_chat/create_chat.html")


@login_required
def room(request, room_name):
    return render(request, "core/video_chat/room.html")
    
    
@login_required
def available_lesson_for_student(request):
    if request.user.is_student:
        return render(request, "core/video_chat/join_chat.html")
    


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

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    
    return JsonResponse({'token': token, 'uid': uid}, safe=False)

