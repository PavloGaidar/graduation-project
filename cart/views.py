from django.shortcuts import render

# Create your views here.
def show_cart(request):
    respose = render(request, "cartapp/cart.html")
    return respose

