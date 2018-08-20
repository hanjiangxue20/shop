from django.contrib import admin

from .models import *


class BlogAdmin(admin.ModelAdmin):
    fields = ['name', 'tagline']
    list_per_page = 10


class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'qq', 'addr']
    list_per_page = 10


class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 10


class TagAdmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
# admin.site.register()
# admin.site.register()
