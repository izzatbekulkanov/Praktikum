from django.contrib import admin
from .models import Contact, Category, News

# Register your models here.

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    def get_ordering(self, request):
        return ['id']

    list_display = ['id', 'name', 'email']
    search_fields = ['name', 'email']
    list_display_links = ['email', 'name']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    def get_ordering(self, request):
        return ['id']

    list_display = ['id', 'title', 'body']
    search_fields = ['title', 'body']
    list_display_links = ['title', 'body']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def get_ordering(self, request):
        return ['id']

    list_display = ['name']
    search_fields = ['name']
    list_display_links = ['name']
