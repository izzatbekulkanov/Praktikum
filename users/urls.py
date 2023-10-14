from django.urls import path
from .views import *


urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),

]