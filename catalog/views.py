from django.shortcuts import render

# Create your views here.
def show_catalog(request):
    respose = render(request, "catalogapp/catalog.html")
    return respose
