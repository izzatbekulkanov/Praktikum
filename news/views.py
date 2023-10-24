from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from hitcount.utils import get_hitcount_model

from .models import Contact, News, Category, Comment
from .forms import ContactForm, CategoryForm, CommentForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
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

from hitcount.views import HitCountDetailView, HitCountMixin


class PostCountHitDetailView(HitCountDetailView):
    model = News
    count_hit = True

def custom_detail_view(request, slug):
    news = get_object_or_404(News, slug=slug)
    context = {}
    #hitcount logikasi
    hit_count = get_hitcount_model().objects.get_for_object(news)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_counted'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits



    comments = news.comments.filter(active=True)
    comment_count = comments.count()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()

            # Redirect to the same page to clear the form and show the new comment
            return redirect('Detail_page', slug=slug)

    else:
        comment_form = CommentForm()

    context = {
        'news': news,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comment_count': comment_count
    }

    return render(request, 'pages/detail_page.html', context)
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
    fields = ('title', 'title_uz', 'title_en', 'title_ru',
               'body', 'body_uz','body_en', 'body_ru',
              'image', 'status', 'category',
              )

    def form_valid(self, form):
        news = form.save(commit=False)
        news.slug = slugify(news.title)
        news.created_time = timezone.now()
        news.updated_time = timezone.now()
        news.save()
        return HttpResponseRedirect(news.get_absolute_url())
class DeleteView(DeleteView):
    model = News
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('main')
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
def delete_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
        category.delete()
    except Category.DoesNotExist:
        # Bunday kategoriya topilmadi
        pass
    return redirect('category_list')

class SearchResultList(ListView):
    model = News
    template_name = 'pages/search_result.html'
    context_object_name = 'results'
    paginate_by = 5  # Sahifada necha element ko'rsatishni tanlash

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        results = context['results']
        context['num_results'] = results.count()
        context['query'] = query
        return context
