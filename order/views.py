import requests
from django.db import models
from django.views.generic import CreateView, ListView

from order.forms import OrderForm
from order.models import OrderHistoryModel
from product.models import Product

token = '6251800251:AAEv86CEuLjyEhyri8t_YQQMktbAE_TTdn8'
chat_id = '1702651852'


class OrderHistory(ListView):
    model = OrderHistoryModel
    template_name = 'pages/order_history.html'
    context_object_name = 'orders'
    paginate_by = 10
    success_url = '/'

    def get_queryset(self):

        if self.request.user.is_authenticated:
            qs = OrderHistoryModel.objects.filter(user=self.request.user).order_by('-created_at')
            return qs
        else:
            return OrderHistoryModel.objects.none()


class Checkout(CreateView):
    form_class = OrderForm
    template_name = 'pages/checkout.html'

    def get_success_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.get_cart_objects(self.request.session.get('cart', [])).order_by('name')
        return context

    def form_valid(self, form):
        qs = Product.get_cart_objects(self.request.session.get('cart', []))
        total_price = qs.aggregate(models.Sum('real_price'))['real_price__sum']
        order = form.save(commit=False)

        if self.request.user.is_authenticated:
            order.user = self.request.user

        order.total_price = total_price
        order.save()  # Save the order first

        # Now set the many-to-many relationship after the order is saved
        order.products.set(qs)

        # send to telegram bot about new order

        # text = f'New order from {form.instance["name"]} {form.cleaned_data["phone"]} {form.cleaned_data["address"]} {form.cleaned_data["email"]} {form.cleaned_data["postal_code"]} {form.cleaned_data["city"]} {form.cleaned_data["country"]} {form.cleaned_data["state"]} '
        text = (f'New order from ' + '\n' +
                f'username = {self.request.user} ' + '\n' +
                f'username = {self.request.user} ' + '\n' +
                f'f_name = {form.instance.first_name} ' + '\n' +
                f'l_name = {form.instance.last_name}' + '\n' +
                f'phone = {form.instance.phone} ' + '\n' +
                f'adress1 = {form.instance.address1}' + '\n' +
                f'address2 = {form.instance.email}' + '\n' +
                f'zip_code= {form.instance.zip_code}' + '\n' +
                f'city =  {form.instance.city}' + '\n' +
                f'country =  {form.instance.country}' + '\n' +
                f'state =  {form.instance.state}'
                )
        products = [f'{product.name} {product.real_price}' for product in qs]
        text += '\n'.join(products) + '\n' + f'total price = {total_price}'
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(url)

        self.request.session['cart'] = []
        return super().form_valid(form)
