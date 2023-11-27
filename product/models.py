from ckeditor.fields import RichTextField
from django.db import models, IntegrityError

from main.models import COllection
from user.models import UserModel


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    @property
    def get_products(self):
        return self.products.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    @property
    def get_products(self):
        return self.products.all()

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    @property
    def get_products(self):
        return self.products.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Colors'


class Size(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    @property
    def get_products(self):
        return self.products.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sizes'


class Brand(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Brands'


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
    collection = models.ForeignKey(COllection, on_delete=models.RESTRICT, related_name='products')
    is_active = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT, related_name='products', null=True, blank=True)

    @property
    def is_sale(self):
        return self.sale_percentage > 0

    @property
    def is_new(self):
        from datetime import datetime, timedelta, timezone
        now = datetime.now(timezone.utc)
        return (now - self.created_at) < timedelta(days=3)

    @property
    def get_sale_price(self):
        return self.price - (self.price * self.sale_percentage / 100)

    @property
    def max_price(self):
        return self.real_price.max()

    @property
    def minprice(self):
        return self.real_price.min()

    @property
    def color_list(self):
        return self.colors.all()

    @property
    def get_tags(self):
        return self.tags.all()

    @property
    def get_colors(self):
        return self.colors.all()

    @property
    def get_sizes(self):
        return self.sizes.all()

    token = '6251800251:AAEv86CEuLjyEhyri8t_YQQMktbAE_TTdn8'
    chat_id = '1702651852'

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ProductModel'
        verbose_name_plural = 'Products'

    @staticmethod
    def get_cart_objects(cart_list):
        return Product.objects.filter(id__in=cart_list)


class WishList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.product.name

    class Meta:
        managed = True
        verbose_name = 'WishList'
        verbose_name_plural = 'WishLists'
        unique_together = ['user', 'product']


class CartModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'CartModel'
        verbose_name_plural = 'CartModels'
        unique_together = ['user', 'product']

    @staticmethod
    def create_or_delete(user, product):
        carted_list = []
        try:
            CartModel.objects.create(user_id=user, product_id=product)
            return product
        except IntegrityError:
            CartModel.objects.filter(user=user, product=product).delete()
            return product
