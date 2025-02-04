from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.hashers import make_password
from .models import User, User_abilities, About_user
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


def payment(request):
    return render(request, "core/payment.html")



def admin_page(request):
    return render(request, "core/admin.html")


def logout_user(request):
    logout(request)
    return redirect("auth:login")



def profile(request):
    if request.method == "GET":
        return render(request, "core/profile.html")



def edit_profile(request):
    if request.method == "GET":
        abilities = User_abilities.objects.all()
        context = {
            "abilities": abilities
        }
        return render(request, "core/profile_edit.html", context)
    if request.method == 'POST':
        pass