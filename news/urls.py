from django.urls import path
from .views import main, error404, contact, category_detail, custom_detail_view, UpdateView, DeleteView, CreateView, category_list, delete_category, SearchResultList




urlpatterns = [
    path('', main, name='main'),
    path('error404/', error404, name='error404'),
    path('contact/', contact, name='contact'),
    path('category/<str:category_name>/', category_detail, name='category_detail'),
    path('news/<slug:slug>/', custom_detail_view, name='Detail_page'),
    path('news/<slug>/edit/', UpdateView.as_view(), name='update_page'),
    path('news/delete/<slug:slug>/', DeleteView.as_view(), name='delete_page'),
    path('create/', CreateView.as_view(), name='create_page'),
    path('category_list/', category_list, name='category_list'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),
    path('result/', SearchResultList.as_view(), name='search')
]
