from django.contrib import admin
from .models import Category, Post, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    class Media:
        js = ['django_tinymce/insert_object.js']
    list_display = ['get_thumbnail_html', 'ShortName']
    list_display_links = ['ShortName']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
