from django.urls import path
from order.views import Checkout,OrderHistory

urlpatterns = [
    path('checkout/', Checkout.as_view(), name='checkouted'),
    path('checkouthistory/', OrderHistory.as_view(), name='checkouthistory'),

]