from django.contrib import admin
from .models import Contact, Category, News

# Contact admin
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    search_fields = ['name', 'email']

# News admin
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('limited_title', 'category', 'status')  # slug ni ko'rsating
    list_filter = ('status', 'category')
    list_editable = ('category', 'status')
    search_fields = ('title', 'body')
    ordering = ('publish_time',)
    prepopulated_fields = {'slug': ('title',)}  # slugni title dan olish

    def limited_title(self, obj):
        max_length = 50
        if len(obj.title) <= max_length:
            return obj.title
        return f"{obj.title[:max_length-3]}..."

    limited_title.short_description = 'Title'

# Category admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
