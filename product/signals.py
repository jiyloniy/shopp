# signal for camputing sale_percentage of product
from django.db.models.signals import pre_save
from django.dispatch import receiver

from product.models import Product


@receiver(pre_save, sender=Product)
def update_product_sale_percentage(sender, instance, **kwargs):
    if instance.price and instance.sale_percentage:
        instance.real_price = instance.price - (instance.price * instance.sale_percentage / 100)
    else:
        instance.real_price = instance.price

