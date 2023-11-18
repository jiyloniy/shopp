from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserModel(AbstractUser):
    country = models.CharField(max_length=100, verbose_name=_('country'), blank=True, null=True)
    address = models.CharField(max_length=200, verbose_name=_('address'), blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name=_('city'), blank=True, null=True)
    region = models.CharField(max_length=200, verbose_name=_('region'), blank=True, null=True)
    zip_code = models.PositiveIntegerField(verbose_name=_('zip code'), blank=True, null=True)
    phone = models.CharField(max_length=13, verbose_name=_('phone'), blank=True, null=True)
    state = models.CharField(max_length=100, verbose_name=_('state'), blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'UserTable'

# seller user and customer user

# seller user
# class Seller(models.Model):
#     user = models.OneToOneField(UserModel, on_delete=models.RESTRICT, related_name='seller')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         verbose_name_plural = 'Sellers'
#
#
# class Customer(models.Model):
#     user = models.OneToOneField(UserModel, on_delete=models.RESTRICT, related_name='customer')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         verbose_name_plural = 'Customers'
