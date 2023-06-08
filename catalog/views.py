from .models import Product, Category, Comment
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
def show_catalog(request):
    context = {"list_products": Product.objects.all(), 'additional_category': Category.objects.all()}
    respose = render(request, "catalogapp/catalog.html", context)
    return respose
def show_product(request):
    response = render(request, 'catalogapp/product.html')
    product_in_cart = ProductInCart.objects.create(
            session_key=session_key, product_id=product_pk)
    context = {'product':get_object_or_404(Product, pk=product_pk)}
