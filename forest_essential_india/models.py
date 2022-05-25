from django.db import models


# Create your models here.


class Product(models.Model):
    image = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    weight = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
