from django.urls import path

from product.views import ProductListView, wishlist, wishedlist, cart_view, ShoppingCartView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('shopcard/', ShoppingCartView.as_view(), name='checkout'),
    path('wishlist/', wishlist, name='wishlist'),
    path('wishes/', wishedlist, name='wished'),
    path('cart/', cart_view, name='cart'),

]
