from .models import Product, Category, Comment
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def show_catalog(request):
    if request.COOKIES.get('LogIn') is not None:
        login = "true"
    else:
        login = 'false'
    if request.method == 'POST':
        if request.POST.get('name') == 'search':
            search_req = request.POST.get('searched-product')
            list_searched = Product.objects.filter(name__contains=search_req)
            if len(list_searched) < 1:
                nothing = f"We don't have a product named {search_req}"
                response = render(request, "catalogapp/search.html", context={'search_req': search_req, 'list_searched': list_searched, 'nothing': nothing,'login':login})
                return response
            response = render(request, "catalogapp/search.html", context={'search_req': search_req, 'list_searched': list_searched,'login':login})
            return response
        else:
            checkedbox = request.POST.getlist('check')
            list_filter = []
            if len(checkedbox) < 1:
                context = {"list_products": None, 'additional_category': Category.objects.all(),'login':login}
                response = render(request, "catalogapp/catalog.html", context)
                return response
            else:
                for box in checkedbox:
                    list_filter.append(Category.objects.get(pk=box))
                list_products = Product.objects.filter(category__in=list_filter)
                context = {"list_products": list_products, 'additional_category': Category.objects.all(),'login':login}
                response = render(request, "catalogapp/catalog.html", context)
                return response

    context = {"list_products": Product.objects.all(), 'additional_category': Category.objects.all(),'login':login}
    response = render(request, "catalogapp/catalog.html", context)
    return response

def show_product(request, product_pk):
    if request.COOKIES.get('LogIn') is not None:
        login = "true"
    else:
        login = 'false'
    product = get_object_or_404(Product, pk=product_pk)
    context = {
        'product': product,
        'list_comment': Comment.objects.filter(product=product),
        'login':login
    }
    response = render(request, 'catalogapp/product.html', context)

    if request.method == 'POST':
        if request.POST.get('name') == 'search':
            search_req = request.POST.get('searched-product')
            list_searched = Product.objects.filter(name__contains=search_req)
            if len(list_searched) < 1:
                nothing = f"We doesn't have product named {search_req}"
                respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'nothing':nothing,'login':login})
                return respose
            respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'login':login})
            return respose
        else:
            if request.POST.get('product_pk') == product_pk:
                if request.COOKIES.get('product') == None:
                    product = product_pk
                    response.set_cookie('product', product)
                    return response
                else:
                    product = request.COOKIES['product'] + ' ' + str(product_pk)
                    response.set_cookie('product', product)
                    return response
            else:
                name = request.POST.get('name-massages')
                messages = request.POST.get('messages')
                Comment.objects.create(name=name, messages=messages, product=product)     
                response = render(request, 'catalogapp/product.html', context)
                return response

    return response
