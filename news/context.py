from unicodedata import category

from .models import Category, News, Contact


def contexts(request):
    # Bu o'zgaruvchi bilan templatlarga o'tkaziladigan ma'lumotlarni tayyorlash
    allNews = News.objects.all().order_by('-publish_time')
    newsuz = News.objects.order_by('-publish_time')[:5]
    newsS = News.objects.filter(category__name='Sport').order_by('-publish_time')
    newsT = News.objects.filter(category__name='Texnologiya').order_by('-publish_time')
    newsX = News.objects.filter(category__name='Xorij').order_by('-publish_time')
    newsM = News.objects.filter(category__name='Mahalliy').order_by('-publish_time')
    categories = Category.objects.all()
    photos = News.objects.all().order_by('-publish_time')
    # news_list = News.objects.filter(category=category)
    
    contexts = {
        "allNews": allNews,
        "newsS": newsS,
        "newsuz": newsuz,
        "newsT": newsT,
        "newsX": newsX,
        "newsM": newsM,
        "categories": categories,
        "photos": photos,
        # "news_list": news_list,
        # "category": category
    }
    return contexts