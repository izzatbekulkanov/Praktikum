from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Contact, News, Category
from .forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

# Create your views here.

# Asosiy sahifa
def main(request):
    return render(request, 'base/main.html')

# Xatolik uchun sahifa
def error404(request):
    return render(request, 'pages/404.html')


# Kontakt form
def contact(request):
    allNews = News.objects.all().order_by('-publish_time')[:6]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Sahifani qaytarish uchun 'return' ishlatish
            return render(request, 'base/main.html')  # 'main' o'rniga o'zingizning shabloningizni qo'yishingiz kerak
    else:
        form = ContactForm()
    context = {
        "allNews": allNews,
        "form": form
    }
    return render(request, 'pages/contact.html', context)




def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    context = {
        "news": news
    }
    return render(request, 'pages/detail_page.html', context)



    # Xar bir malumot uchun klasdan foydalanilgan detail page
# class Detail_page(DetailView):
#     model = News
#     template_name = 'pages/detail_page.html'  # HTML-shablon nomi
#     context_object_name = 'news'  # Context o'zgaruvchi nomi
    
#     def get_object(self, queryset=None):
#         slug = self.kwargs.get('slug')
#         if slug:
#             try:
#                 return self.model.objects.get(slug=slug)
#             except self.model.DoesNotExist:
#                 raise Http404("News does not exist")
#         else:
#             return None