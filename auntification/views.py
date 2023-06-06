from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def show_registration(request):
    response  = render(request, "auntificationapp/reg.html")
    if request.method == "GET" and request.COOKIES.get('LogIn') is not None:
        return redirect('../')
    if request.method == "POST":
        # записуємо данні з форми в змінні
        UserNew = User(name=request.POST.get('name'),password=request.POST.get('password'), phone=request.POST.get('phone'),email=request.POST.get('email'))
        UserNew.save()
        response.set_cookie('LogIn', True)
        return response
    return response 




def show_login(request):
    response  = render(request, "auntificationapp/login.html")
    if request.method == "GET" and request.COOKIES.get('LogIn') is not None:
        return redirect('../')
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = User(request, name = name, password = password)
        
    return response
    
def show_login(request):
    context = {}
    response  = render(request, "auntificationapp/login.html")
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        user = User(request, name = name, password = password)
        if user != None:
            response.set_cookie('LogIn', True)
            context["error_text"] = ""
            return response
            
        else:
            context["error_text"] = "Oh no, There was mistake nickname or password are incorect"
    return response
