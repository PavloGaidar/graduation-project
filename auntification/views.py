from django.shortcuts import render,redirect 
from .models import User
from django.db.utils import IntegrityError


# Create your views here.
def show_registration(request):
    context={}
    response  = render(request, "auntificationapp/reg.html")
    if request.method == "GET" and request.COOKIES.get('LogIn') is not None:
        return redirect('../')
    if request.method == "POST":
        name=request.POST.get('name')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        users = User.objects.all()
        for user in users:
            if name != user.name:
                if email != user.email:
                    if phone != user.phone:
                        UserNew = User(name=request.POST.get('name'),password=request.POST.get('password'),phone=request.POST.get('phone'),email=request.POST.get('email'))
                        UserNew.save()
                        response.set_cookie('LogIn', True)
                        print('succes')
                        response  = render(request, "auntificationapp/reg.html")
                        return response
                    else:
                        context['error_text']= 'Phone number is already taken'
                        print("phone")
                        response  = render(request, "auntificationapp/reg.html", context)
                        return response
                else:
                    context['error_text']= 'Email is already taken'
                    print("email")
                    response  = render(request, "auntificationapp/reg.html", context)
                    return response
            else:
                context['error_text']= 'Nickname is already taken'
                print("name")
                response  = render(request, "auntificationapp/reg.html", context)
                return response
        else:
            context['error_text']= 'Паролі не співпадають!'
            response  = render(request, "auntificationapp/reg.html", context)
            return response

    return response 

def show_login(request):
    context={}
    response = render(request, "auntificationapp/login.html")
    if request.method == "GET" and request.COOKIES.get('LogIn') is not None:
        return redirect('../')
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        users = User.objects.all()

        user = User.objects.filter(name=name, password=password)
        print(user)
        if user != None:
            print('пройшло')
            response.set_cookie('LogIn', True)
            return response
        else:
            print('не пройшло')
            response = render(request, "auntificationapp/login.html", context={'error' : 'true'})
        for user in users:
            return response
        else:
            context['error_text']= 'Паролі не співпадають!'
            response  = render(request, "auntificationapp/login.html", context)
            return response
    return response