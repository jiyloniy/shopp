from django import forms

from product.models import Color


class ColorForm(forms.ModelForm):
    name = forms.CharField(
        label='Color name',
        widget=forms.TextInput(attrs={'type': 'color'})
    )

    class Meta:
        model = Color
        fields = '__all__'
