from .models import Product, Category, Comment
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
def show_catalog(request):
    context = {"list_products": Product.objects.all(), 'additional_category': Category.objects.all()}
    respose = render(request, "catalogapp/catalog.html",  context)
    return respose
def show_product(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    response = render(request, 'catalogapp/product.html',context={'product':product})
    if request.method == 'POST':
        if request.COOKIES.get('product') == None:
            product = product_pk
            response.set_cookie('product', product)
            return response
        else:
            product = request.COOKIES['product'] + ' ' + str(product_pk)
            response.set_cookie('product', product)
            return response
    return response