from django.shortcuts import render

# Create your views here.
def all_users(request):
    return render(request, "core/bilim_users.html")



def exact_user(request):
    return render(request, "core/bilim_exact_user.html")