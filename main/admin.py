from django.contrib import admin

from main.models import Contact, Team, Banner, COllection


@admin.register(COllection)
class COllectionAdmin(admin.ModelAdmin):
    libs_display = ['name', 'created_at', 'updated_at']
    list_filter = ['name', 'created_at', 'updated_at']


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position', 'image']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['collection', 'title', 'description', 'created_at', 'image', 'is_active']
    list_filter = ['collection', 'title', 'created_at', 'is_active']
