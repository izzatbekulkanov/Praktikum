from django.db import models

# Create your models here.


class Contact(models.Model):
    name = CharField(max_length)