from django.db import models
from Products.models import *


class userDetails(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=50, primary_key=True)
    contact_no = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    address = models.CharField(max_length=300)


class Cart(models.Model):
    email = models.ForeignKey(userDetails, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


# class OrderDetails(models.Model):
#     email = models.ForeignKey(userDetails,on_delete=models.CASCADE)
#     productId = models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)


class Franchise(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)


class User_Orders(models.Model):
    email = models.ForeignKey(userDetails, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    order_time = models.DateTimeField()

class Order_Products(models.Model):
    order_id = models.ForeignKey(User_Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# Create your models here.
