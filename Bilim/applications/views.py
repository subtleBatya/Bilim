from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Application
from videos.models import Video_category
# Create your views here.
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
