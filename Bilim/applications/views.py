from django.shortcuts import render

# Create your views here.
def application(request):
    return render(request, "core/application.html")