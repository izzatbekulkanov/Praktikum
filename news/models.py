from django.db import models
from django.utils import timezone
from django.urls import reverse


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
    class Meta:
        ordering = ["publish_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Detail_page", args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

class Contact(models.Model):
    name = models.CharField(max_length=140)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email