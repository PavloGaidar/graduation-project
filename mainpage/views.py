from django.shortcuts import render
from catalog.models import Product

# Create your views here.
def show_mainpage(request):
    if request.method == 'POST':
        print('343')
        search_req = request.POST.get('searched-product')
        list_searched = Product.objects.filter(name__contains=search_req)
        if len(list_searched) < 1:
            nothing = f"We doesn't have product named {search_req}"
            respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched,'nothing':nothing})
            return respose
        respose = render(request, "catalogapp/search.html",context={'search_req':search_req,'list_searched':list_searched})
        return respose
    respose = render(request, "mainpageapp/mainpage.html")
    return respose