from .models import Product, Category, Comment
from django.shortcuts import render

# Create your views here.
def show_catalog(request):
    context = {"list_products": Product.objects.all(), 'additional_category': Category.objects.all()}
    respose = render(request, "catalogapp/catalog.html", context)
    return respose
