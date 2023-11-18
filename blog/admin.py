from django.contrib import admin

from blog.models import Blog, Tag, Author, Comment


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']

    readonly_fields = ['slug']
