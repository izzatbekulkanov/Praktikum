from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Contact, News, Category
from .forms import ContactForm
from django.urls import reverse_lazy

# Create your views here.


def main(request):
    allNews = News.objects.all().order_by('-publish_time')
    news = News.objects.all().order_by('-publish_time')[:5]
    newsS = News.objects.filter(category__name='Sport').order_by('-publish_time')
    newsT = News.objects.filter(category__name='Texnologiya').order_by('-publish_time')
    newsX = News.objects.filter(category__name='Xorij').order_by('-publish_time')
    newsM = News.objects.filter(category__name='Mahalliy').order_by('-publish_time')
    categories = Category.objects.all()
    photos = News.objects.all().order_by('-publish_time')[:9]

    context = {
        "allNews": allNews,
        "newsS": newsS,
        "news": news,
        "newsT": newsT,
        "newsX": newsX,
        "newsM": newsM,
        "categories": categories,
        "photos": photos,
    }
    return render(request, 'base/main.html', context)
def error404(request):
    return render(request, 'pages/404.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Sahifani qaytarish uchun 'return' ishlatish
            return render(request, 'base/main.html')  # 'main' o'rniga o'zingizning shabloningizni qo'yishingiz kerak
    else:
        form = ContactForm()
    context = {
        "form": form
    }
    return render(request, 'pages/contact.html', context)

def single_page(request):
    return render(request, 'pages/single_page.html')
