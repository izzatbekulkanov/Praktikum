from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number']  # Ro'yxatda ko'rsatiladigan maydonlar
    # Qo'shimcha sozlamalar

admin.site.register(CustomUser, CustomUserAdmin)