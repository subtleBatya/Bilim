from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.hashers import make_password
from .models import User, User_abilities
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


def payment(request):
    return render(request, "core/payment.html")



def admin_page(request):
    return render(request, "core/admin.html")

#ready function
def logout_user(request):
    logout(request)
    return redirect("auth:login")


#ready function
def profile(request):
    if request.method == "GET":
        if request.user.is_student:
            return render(request, "core/profile.html")


#ready function
def edit_profile(request):
    if request.method == "GET":
        abilities = User_abilities.objects.all()
        context = {
            "abilities": abilities
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
