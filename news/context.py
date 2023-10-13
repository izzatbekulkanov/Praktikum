from .models import Category, News, Contact


def contexts(request):
    # Bu o'zgaruvchi bilan templatlarga o'tkaziladigan ma'lumotlarni tayyorlash
    allNews = News.objects.all().order_by('-publish_time')
    news = News.objects.all().order_by('-publish_time')[:5]
    newsS = News.objects.filter(category__name='Sport').order_by('-publish_time')
    newsT = News.objects.filter(category__name='Texnologiya').order_by('-publish_time')
    newsX = News.objects.filter(category__name='Xorij').order_by('-publish_time')
    newsM = News.objects.filter(category__name='Mahalliy').order_by('-publish_time')
    categories = Category.objects.all()
    photos = News.objects.all().order_by('-publish_time')[:9]
    lastNewsT = News.objects.filter(category__name='Texnologiya').latest('publish_time')
    lastNewsX = News.objects.filter(category__name='Xorij').latest('publish_time')
    lastNewsS = News.objects.filter(category__name='Sport').latest('publish_time')
    lastNewsM = News.objects.filter(category__name='Mahalliy').latest('publish_time')
    

    
    contexts = {
        "allNews": allNews,
        "newsS": newsS,
        "news": news,
        "newsT": newsT,
        "newsX": newsX,
        "newsM": newsM,
        "categories": categories,
        "photos": photos,
        "lastNewsT": lastNewsT,
        "lastNewsX": lastNewsX,
        "lastNewsS": lastNewsS,
        "lastNewsM": lastNewsM,
    }
    return contexts