# signals
from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Product


#
@receiver(post_save, sender=Product)
def sale(sender, instance, created, **kwargs):
    if instance.sale_percentage:
        instance.real_price = instance.price - (instance.price * instance.sale_percentage / 100)
        instance.save()
    else:
        instance.real_price = instance.price
        instance.save()

    return instance


