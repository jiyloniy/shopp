from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CommentForm
from blog.models import Blog, Comment


class BlogView(ListView):
    template_name = "pages/blog.html"
    model = Blog
    paginate_by = 9

    def get_queryset(self):
        qs = Blog.objects.all()
        tag = self.request.GET.get('tag', '')
        if tag:
            qs = qs.filter(tags__name=tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.request.GET.get('tag', '')
        if tag:
            context['tag'] = tag
        return context


class BlogDetail(DetailView):
    template_name = 'pages/blog-details.html'
    model = Blog

    # get blogs after and before from blog dont use created_at
    # path = slug

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     con
    #
    #     return context


# save post and add coment for given id of blog
def com(request, slug):
    print(request.POST)
    if request.method == 'POST':
        print(request.POST)
        form = CommentForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            # send  telegram bot
            token = Comment.token
            chat_id = Comment.chat_id
            blog = Blog.objects.get(slug=slug)
            text = f'Blog: {blog.title}\nName: {form.instance.name}\nEmail: {form.instance.email}\nPhone: {form.instance.phone}\nComment: {form.instance.comment}'
            url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
            import requests
            requests.get(url)

            blog.comments.add(form.instance)
            blog.save()

    return redirect('blogdeteil', slug=slug)


class CommentCreateView(CreateView):
    form_class = CommentForm
    model = Blog

    def form_valid(self, form):
        blog = Blog.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        token = Comment.token
        chat_id = Comment.chat_id
        text = f'Blog: {blog.title}\nName: {form.instance.name}\nEmail: {form.instance.email}\nPhone: {form.instance.phone}\nComment: {form.instance.comment}'
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        import requests
        requests.get(url)
        blog.comments.add(form.instance)
        blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogdeteil', kwargs={'slug': self.kwargs.get('slug')})
