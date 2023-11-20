from django.views.generic import ListView

from product.models import Product, Category, Tag, Color, Size,COllection


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'pages/shop.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(is_active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['categories'] = Category.objects.filter(is_active=True)
        data['tags'] = Tag.objects.filter(is_active=True)
        data['colors'] = Color.objects.filter(is_active=True)
        data['sizes'] = Size.objects.filter(is_active=True)
        data['collections'] = COllection.objects.filter(is_active=True)
        return data

