from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

# Create your views here.



def show_cart(request):
        if request.COOKIES.get('product') is not None:
            products_pk = request.COOKIES['product'].split(' ')
            list_products = list()
            for product in products_pk:
                list_products.append(Product.objects.get(pk=product))
            response = render(request, 'cartapp/cart.html', {'products': list_products})
        else:
            list_products = list()
            response = render(request, 'cartapp/cart.html', {'products': list_products})

        if request.method == 'POST':
            pk_deleted = request.POST.get('product_pk')

            if pk_deleted:
                products_pk.remove(pk_deleted)
                new_product = ' '.join(products_pk)

                if new_product:
                    list_products = list()
                    for product in new_product.split(" "):
                        list_products.append(Product.objects.get(pk=product))
                    response = render(request, 'cartapp/cart.html', {'products': list_products})
                    response.set_cookie('product', new_product)
                    return response
                else:
                    response = render(request, 'cartapp/cart.html', {'products': []})
                    response.delete_cookie('product')
                    return response

        return response
