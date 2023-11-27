from django.db import models
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from product.models import Product, Category, Tag, Color, Size, COllection, Brand, WishList


class ShoppingCartView(ListView):
    template_name = 'pages/shopping-cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return Product.get_cart_objects(cart)


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'pages/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        qs = Product.objects.all()
        q = self.request.GET.get('q', '')
        cat = self.request.GET.get('cat', '')  # for category filter
        tag = self.request.GET.get('tag', '')
        color = self.request.GET.get('color', '')
        size = self.request.GET.get('size', '')
        collection = self.request.GET.get('collection', '')
        brand = self.request.GET.get('brand', '')
        price = self.request.GET.get('price', '')

        print(price)
        if q:
            qs = qs.filter(name__icontains=q)
        if cat:
            qs = qs.filter(category__pk=cat)
        if tag:
            qs = qs.filter(tags__pk=tag)

        if color:
            qs = qs.filter(colors__pk=color)
        if size:
            qs = qs.filter(sizes__pk=size)
        if collection:
            qs = qs.filter(colors__pk=collection)
        if brand:
            qs = qs.filter(brand__pk=brand)

        if price:
            price = price.split(';')
            qs = qs.filter(real_price__gte=price[0], real_price__lte=price[1])

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['categories'] = Category.objects.filter(is_active=True)
        data['tags'] = Tag.objects.filter(is_active=True)
        data['colors'] = Color.objects.filter(is_active=True)
        data['sizes'] = Size.objects.filter(is_active=True)

        data['collections'] = COllection.objects.all()
        data['brands'] = Brand.objects.all()
        data['max_price'], data['min_price'] = Product.objects.all().aggregate(models.Max('real_price'),
                                                                               models.Min('real_price')).values()
        return data


def wishlist(request):
    a = request.GET.get('product_id')
    b = request.GET.get('product_delete_id')

    if b:
        product = Product.objects.filter(pk=b).first()
        WishList.objects.filter(user=request.user, product=product).delete()
    else:
        product = Product.objects.filter(pk=a).first()
        if not WishList.objects.filter(user=request.user, product=product).exists():
            WishList.objects.create(user=request.user, product=product)
    return HttpResponse('', status=200)


def wishedlist(request):
    user = request.user
    wishes = WishList.objects.filter(user=user)
    object_list = []
    for wish in wishes:
        object_list.append(wish.product)
    context = {
        'object_list': object_list
    }
    return render(request, 'pages/wishes_list.html', context)


def cart_view(request):
    #  /product/cart/?product_id=6
    id = int(request.GET.get('product_id'))

    cart = request.session.get('cart', [])
    if not cart:
        request.session['cart'] = []
        cart = request.session['cart']

    if id not in cart:
        cart.append(id)
        request.session['cart'] = cart
    else:
        cart.remove(id)
        request.session['cart'] = cart
    print(request.session['cart'])
    return HttpResponse('', status=200)



