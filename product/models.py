from ckeditor.fields import RichTextField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Colors'


class Size(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sizes'


# Create your models here.

class Product(models.Model):
    img_field = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    long_description = RichTextField()
    real_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_percentage = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='products')
    tags = models.ManyToManyField(Tag, related_name='products')
    colors = models.ManyToManyField(Color, related_name='products')
    sizes = models.ManyToManyField(Size, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_sale(self):
        return self.sale_percentage > 0

    @property
    def get_sale_price(self):
        return self.price - (self.price * self.sale_percentage / 100)

    @property
    def get_tags(self):
        return self.tags.all()

    @property
    def get_colors(self):
        return self.colors.all()

    @property
    def get_sizes(self):
        return self.sizes.all()

    # @property
    # def send_from_telegram_bot(self):
    #     token = '6251800251:AAEv86CEuLjyEhyri8t_YQQMktbAE_TTdn8'
    #     chat_id = '1702651852'
    #     text = f'Name: {self.name}\nPrice: {self.price}\nSale Percentage: {self.sale_percentage}'
    #     url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    #     self.send_request(url)
    #     return True
    #
    # @staticmethod
    # def send_request(url):
    #     import requests
    #     requests.get(url)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ProductModel'
        verbose_name_plural = 'Products'
