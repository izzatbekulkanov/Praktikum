from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.http import Http404
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class News(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft
                              )
    def save(self, *args, **kwargs):
        if not self.slug:  # Agar slug bo'sh bo'lsa
            self.slug = slugify(self.title)  # title dan slug yaratish
        super(News, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ["publish_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Detail_page", args=[str(self.slug)])


class Contact(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email
class Comment (models.Model):
    news = models.ForeignKey(News,
                             on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return f"Comment = {self.body} by {self.user}"


