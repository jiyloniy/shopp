from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='author/')

    @property
    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    token = '6057040672:AAGv4RwJnT3z9jFgd4iugf_i2IyV7k7IxTc'
    chat_id = '1702651852'

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    main_title = RichTextField()
    main_page = models.ImageField(upload_to='main/')
    detail_img = models.ImageField(upload_to='detail/')
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, related_name='blogs')
    comments = models.ManyToManyField(Comment, related_name='blogs', blank=True)
    tags = models.ManyToManyField(Tag, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)

    @property
    def get_tags(self):
        return self.tags.all()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogdeteil', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'BlogTable'
        verbose_name_plural = 'Blogs'
        ordering = ['-id']
