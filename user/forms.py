from django import forms
from django.utils.translation import gettext_lazy as _

from user.models import UserModel, ProfileModel


class UserRegisterForm(forms.Form):
    # fields = ['first_name', 'last_name', 'username', 'password', 'password2']
    first_name = forms.CharField(max_length=100, label=_('first name'))
    last_name = forms.CharField(max_length=100, label=_('last name'))
    username = forms.CharField(max_length=100, label=_('username'))
    password = forms.CharField(max_length=100, label=_('password'), widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label=_('password confirmation'), widget=forms.PasswordInput)

    def clean_username(self):
        print(5555555555)
        username = self.cleaned_data.get('username')
        if UserModel.objects.filter(username=username).exists():
            print('test')
            raise forms.ValidationError(_('Brat mashi xato'))
        return username

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if not password == password2:
            raise forms.ValidationError(_('passwords do not match'))
        return password2


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label=_('username'))
    password = forms.CharField(max_length=100, label=_('password'), widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not UserModel.objects.filter(username=username).exists():
            raise forms.ValidationError(_('username or password is incorrect'))
        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = UserModel.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError(_('username or password is incorrect'))
        return password


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['user']
        fields = '__all__'

