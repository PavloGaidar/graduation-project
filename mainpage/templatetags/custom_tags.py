from django import template

register = template.Library()

@register.simple_tag 
def count_products_in_cart(request):
    products_in_cart = request.COOKIES.get('product').split(' ')
    products_count = len(products_in_cart)
    if products_count == 0:
        pass
    else:
        return products_count