from django.views.generic import ListView

from product.models import Product, Category, Tag, Color, Size, COllection, Brand


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'pages/shop.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        qs = Product.objects.all()
        q = self.request.GET.get('q', '')
        cat = self.request.GET.get('cat', '')  # for category filter
        tag = self.request.GET.get('tag', '')
        color = self.request.GET.get('color', '')
        size = self.request.GET.get('size', '')
        collection = self.request.GET.get('collection', '')
        brand = self.request.GET.get('brand', '')
        if q:
            qs = qs.filter(name__icontains=q)
        if cat:
            qs = qs.filter(category__name__icontains=cat)
        if tag:
            qs = qs.filter(tags__name__icontains=tag)
        if color:
            qs = qs.filter(colors__name__icontains=color)
        if size:
            qs = qs.filter(sizes__name__icontains=size)
        if collection:
            qs = qs.filter(collection__name__icontains=collection)
        if brand:
            qs = qs.filter(brand__name__icontains=brand)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=None, **kwargs)
        data['categories'] = Category.objects.filter(is_active=True)
        data['tags'] = Tag.objects.filter(is_active=True)
        data['colors'] = Color.objects.filter(is_active=True)
        data['sizes'] = Size.objects.filter(is_active=True)

        data['collections'] = COllection.objects.all()
        data['brands'] = Brand.objects.all()
        return data
