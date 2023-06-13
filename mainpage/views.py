from django.shortcuts import render
# Create your views here.
def show_mainpage(request):
    respose = render(request, "mainpageapp/mainpage.html")
    return respose