from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product

# Create your views here.



def show_cart(request):
    




        products_pk = request.COOKIES['product'].split(' ')
        list_products = Product.objects.filter(pk__in=products_pk)
        response = render(request, 'cartapp/cart.html', {'products': list_products})

        if request.method == 'POST':
            pk_deleted = request.POST.get('product_pk')

            if pk_deleted:
                products_pk.remove(pk_deleted)
                new_product = ' '.join(products_pk)

                if new_product:
                    list_products = Product.objects.filter(pk__in=products_pk)
                    response.set_cookie('product_pk', new_product)
                    
                else:
                    response = render(request, 'cartapp/cart.html', {'products': []})
                    response.delete_cookie('product_pk')

        return response
