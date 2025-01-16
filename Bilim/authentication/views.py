from django.shortcuts import render

def login(request):
    return render(request, "core/login.html")



def sign_up(request):
    return render(request, "core/sign_up.html")


def payment(request):
    return render(request, "core/payment.html")



def admin_page(request):
    return render(request, "core/admin.html")
