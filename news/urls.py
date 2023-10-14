from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='main'),
    path('error404/', error404, name='error404'),
    path('contact/', contact, name='contact'),
    path('news/<slug:slug>/', CustomDetailView.as_view(), name='Detail_page')
    # path('news/<slug:slug>/', news_detail, name='Detail_page')
]

# path('tour_about/', tour_about, name='tour_about'),
    # path('tour_elements/<slug:slug>/', tour_elements, name='tour_elements'),
    # path('tour_detail/<slug:slug>/', tour_detail, name='tour_detail'),
    # path('create/', TourCreateView.as_view(), name='create'),
    # path('delete/<int:pk>/', TourDeleteView.as_view(), name='delete'),
    # path('update/<int:pk>/', TourUpdateView.as_view(), name='update'),
    # path('tours/', TourListView.as_view(), name='allTour'),