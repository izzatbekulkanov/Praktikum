from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='profile_pics/', default='static/images/default.webp', blank=True, null=True)
    data_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} profili"
