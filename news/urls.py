from django.urls import path
from .views import main, error404, contact, category_detail, CustomDetailView, UpdateView, DeleteView, CreateView, category_list, delete_category




urlpatterns = [
    path('', main, name='main'),
    path('error404/', error404, name='error404'),
    path('contact/', contact, name='contact'),
    path('category/<str:category_name>/', category_detail, name='category_detail'),
    path('news/<slug:slug>/', CustomDetailView.as_view(), name='Detail_page'),
    path('news/<slug>/edit/', UpdateView.as_view(), name='update_page'),
    path('news/delete/<slug:slug>/', DeleteView.as_view(), name='delete_page'),
    path('create/', CreateView.as_view(), name='create_page'),
    path('category_list/', category_list, name='category_list'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),

]

# path('tour_about/', tour_about, name='tour_about'),
    # path('tour_elements/<slug:slug>/', tour_elements, name='tour_elements'),
    # path('tour_detail/<slug:slug>/', tour_detail, name='tour_detail'),
    # path('create/', TourCreateView.as_view(), name='create'),
    # path('delete/<int:pk>/', TourDeleteView.as_view(), name='delete'),
    # path('update/<int:pk>/', TourUpdateView.as_view(), name='update'),
    # path('tours/', TourListView.as_view(), name='allTour'),