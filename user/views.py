from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from user.forms import LoginForm, UserRegisterForm, ProfileModelForm
from user.models import UserModel, ProfileModel


# Create your views here.

class ProfileView(LoginRequiredMixin,UpdateView):
    form_class = ProfileModelForm
    template_name = 'pages/profile.html'

    def get_success_url(self):
        return reverse('profile')

    def get_object(self, queryset=None):
        profile, created = ProfileModel.objects.get_or_create(user=self.request.user)
        return profile


def Login(request):
    form = LoginForm()
    if request.user.is_authenticated:
        message = 'You are already logged in'

        return redirect('home')
    else:
        if request.method == 'POST':
            if request.user.is_authenticated:
                return redirect('home')
            else:
                form = LoginForm(request.POST)
                if form.is_valid():
                    print(form.cleaned_data)
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(username=username, password=password)
                    if user:
                        login(request, user)
                        return redirect('home')

    return render(request, 'pages/login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        message = 'You are already logged in'

        return redirect('home')

    form = UserRegisterForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserRegisterForm(request.POST)

            if form.is_valid():
                print(666666)
                user = UserModel.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password'),
                    first_name=form.cleaned_data.get('first_name'),
                    last_name=form.cleaned_data.get('last_name'),
                )
                login(request, user)
                return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'pages/registration.html', context)


def log(request):
    logout(request)
    return redirect('home')
