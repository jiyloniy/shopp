from django.db import models
from django.template.defaultfilters import register

from product.models import Product, WishList


@register.simple_tag
def get_current_price(request, index=0):
    price = request.GET.get('price', '2').split(';')

    if price == ['2']:
        return 'null'
    else:
        return float(price[index])


@register.simple_tag
def cart(request):
    birnima = request.session.get('cart', [])
    objects = Product.objects.filter(pk__in=birnima).aggregate(models.Sum('real_price'))['real_price__sum']
    if objects is None:
        return 0.0, 0
    else:
        return objects, len(birnima)


@register.simple_tag()
def cart_info(request):
    return Product.get_cart_objects(request)


@register.filter()
def is_wishlist(product, request):
    return WishList.objects.filter(user=request.user, product=product).exists()


@register.filter()
def is_cart(product, request):
    return product.id in request.session.get('cart', [])
