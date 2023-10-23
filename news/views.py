from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact, News, Category
from .forms import ContactForm, CategoryForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import Http404
from setting.custom_permissions import OnlyLoggedSuperUser
from django.utils.text import slugify
from django.utils import timezone
from django.views import View

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



class CustomDetailView(DetailView):
    model = News
    template_name = 'pages/detail_page.html'
    context_object_name = 'news'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        if slug:
            try:
                return self.model.objects.get(slug=slug)
            except self.model.DoesNotExist:
                raise Http404("News does not exist")
        else:
            return None

def category_detail(request, category_name):
    # Kategoriyaga oid ma'lumotlarni olish uchun kerakli so'rovni yozing
    category = Category.objects.get(name=category_name)
    news_list = News.objects.filter(category=category)
    context = {
        "category_name": category_name,
        "news_list": news_list,
        "active_category": category_name,  # active_category o'zgaruvchisini aniqlang
    }
    return render(request, 'pages/news.html', context)

class UpdateView(UpdateView):
    model = News
    template_name = 'pages/update.html'
    context_object_name = 'news'
    fields = ('title', 'body', 'image', 'status', 'category')
    success_url = reverse_lazy('main')

class CreateView(OnlyLoggedSuperUser, CreateView):
    model = News
    template_name = 'pages/create.html'
    context_object_name = 'news'
    fields = ('title', 'body', 'image', 'status', 'category')

    def form_valid(self, form):
        news = form.save(commit=False)
        news.slug = slugify(news.title)
        news.created_time = timezone.now()
        news.updated_time = timezone.now()
        news.save()
        return HttpResponseRedirect(news.get_absolute_url())
def category_list(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = Category.objects.create(name=name)
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'pages/category.html', {'categories': categories, 'form': form})
class DeleteView(DeleteView):
    model = News.category
    template_name = 'pages/category.html'
    success_url = reverse_lazy('create_page')

def delete_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
        category.delete()
    except Category.DoesNotExist:
        # Bunday kategoriya topilmadi
        pass
    return redirect('category_list')
