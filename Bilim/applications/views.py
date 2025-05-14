from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Application
from videos.models import Video_category

#API VIEWS
from rest_framework.decorators import api_view
from rest_framework import status 
from rest_framework.response import Response
from .serializer import ApplicationSerializer

# All views
@login_required
def application(request):
    if request.method == "GET":
        courses = Video_category.objects.all()
        context = {
            "courses":courses
        }
        return render(request, "core/application.html", context)
    if request.method == "POST":
        application = request.POST.get("application")
        user = request.user
        user_application = Application.objects.create(application_owner=user, application_text=application )
        try:
            user_application.save()
            return redirect("core:success")
        except:
            return redirect("core:error")
        

@login_required
@api_view(["GET"])
def api_application(request):
    applications = Application.objects.all()
    serialized_data = ApplicationSerializer(applications, many=True).data
    return Response(serialized_data)


@login_required
@api_view(["POST"])
def api_application_create(request):
    data = request.data
    serializer = ApplicationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED )
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

