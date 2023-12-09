# Create your views here.
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView

from blog.models import Blog
from main.models import Contact, Banner
from .forms import ContactForm


# Create your models here.

class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.filter(is_active=True).order_by('-id')
        context['blogs'] = Blog.objects.all().order_by('-id')[:3]
        return context


def home(request):
    return render(request, 'pages/index.html')


class ContactView(CreateView):
    template_name = 'pages/contact.html'
    model = Contact
    fields = ['name', 'email', 'message']

    # send to bot

    def form_valid(self, form):
        print(form.instance)
        form.save()
        # send  telegram bot
        token = Contact.token
        chat_id = Contact.chat_id
        text = f'Name: {form.instance.name}\nEmail: {form.instance.email}\nMessage: {form.instance.message}'
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        import requests
        requests.get(url)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact')


def contact(request):
    print(request.GET)
    print(request.POST)
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            token = Contact.token
            chat_id = Contact.chat_id
            text = f'Name: {form.instance.name}\nEmail: {form.instance.email}\nMessage: {form.instance.message}'
            url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            import requests

            return reverse('contact')
        else:
            print(form.errors)
            return render(request, 'pages/contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})
