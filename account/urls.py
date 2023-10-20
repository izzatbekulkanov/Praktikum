from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from .views import *


urlpatterns = [
    path('signup/', user_register, name='signup'),
    path('signup-done/', singup_done, name='signup_done'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('edit-user/', edit_user, name='edit_user'),
    path('recent/', recent, name='recent'),


]