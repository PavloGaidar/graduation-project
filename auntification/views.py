from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def show_registration(request):
    response  = render(request, "auntificationapp/reg.html")
    if request.method == "POST":
        # записуємо данні з форми в змінні
        nameUser = request.POST.get('name')
        passwordUser = request.POST.get('password')
        pictureUser = request.POST.get('image')
        emailUser = request.POST.get('email')
        User.objects.create(name = nameUser, password = passwordUser, picture=pictureUser,email=emailUser)
        return redirect("  ")
    return response 
