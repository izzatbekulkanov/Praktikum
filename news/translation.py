from modeltranslation.translator import register, TranslationOptions
from .models import News, Category

@register(News)
class NewsTranslateionOptions(TranslationOptions):
    fields = ('title', 'body')

@register(Category)
class CategoryTranslateionOptions(TranslationOptions):
    fields = ('name',)
