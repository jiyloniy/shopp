from django.forms import ModelForm

from order.models import OrderHistoryModel


class OrderForm(ModelForm):
    class Meta:
        model = OrderHistoryModel
        fields = '__all__'
        exclude = ['user', 'products', 'total_price', 'created_at']
