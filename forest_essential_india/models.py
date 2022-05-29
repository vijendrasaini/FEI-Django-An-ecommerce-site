from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):
    image = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    weight = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    category = models.CharField(max_length=20)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.BigIntegerField()
    product_qty = models.IntegerField(default=1)

