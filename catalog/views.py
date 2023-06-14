from .models import Product, Category, Comment
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
def show_catalog(request):
    context = {"list_products": Product.objects.all(), 'additional_category': Category.objects.all()}
    respose = render(request, "catalogapp/catalog.html",  context)
    return respose

def show_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    context = {
        'product': product,
    }

    response = render(request, 'catalogapp/product.html', context)

    if request.method == 'POST':
        name = request.POST.get('name-massages')
        messages = request.POST.get('messages')
        Comment.objects.create(name=name, messages=messages, product=product)

        if request.COOKIES.get('product') is None:
            product_cookie = str(product_pk)
        else:
            product_cookie = request.COOKIES['product'] + ' ' + str(product_pk)
        
        response.set_cookie('product', product_cookie)
        
        return response

    return response
# def show_product(request, product_pk):
#     product = Product.objects.get(pk=product_pk)
#     context = {
#         'product':product,

#     }

#     response = render(request, 'catalogapp/product.html',context)

#     if request.method == 'POST':
#         name = request.POST.get('name-massages')
#         massages = request.POST.get('messages')
#         Comment.objects.create(name = name, messages = massages,product=Comment.objects.filter(pk=product_pk) )
       
#         if request.COOKIES.get('product') == None:
#             product = product_pk
#             response.set_cookie('product', product)
#             return response
#         else:
#             product = request.COOKIES['product'] + ' ' + str(product_pk)
#             response.set_cookie('product', product)
#             return response
#     return response
