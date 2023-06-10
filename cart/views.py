from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

# Create your views here.
def show_cart(request):
    if request.COOKIES.get('product') is not None: #
        
        products = request.COOKIES['product']
        products = products.split(' ')

        list_products = list()
        for product in products:
            list_products.append(Product.objects.get(pk=product))
        response = render(request,"cartapp/cart.html",context={"products": list_products})
    else:
        response = render(request,"cartapp/cart.html",context={"products":list()})

        
    if request.method == "POST":
        print(request.POST.get('index'))
        # products = request.COOKIES['product'].split(' ')
        # if request.POST.get('name') == 'delete':
        #     if len(request.COOKIES['product'].split(' ')) > 1:
        #         product = request.POST.get('item') + "_" + request.POST.get('amount')
        #         products.remove(product)
        #         products = " ".join(products)
        #         print(products)
        #         response.set_cookie('product', products)
        #         return response
        #     else:
        #         response.delete_cookie('product')
        #         return response


    return response

    