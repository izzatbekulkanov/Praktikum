from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Telefon raqami (misol: +998901234567)

    objects = CustomUserManager()  # Bu yerda CustomUserManager'ni qo'shing