from django.db import models

from product.models import Product
from user.models import UserModel


class OrderHistoryModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=125)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=6)
    email = models.EmailField(null=True)
    total_price = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    @property
    def get_all_products(self):
        return self.products.all()
