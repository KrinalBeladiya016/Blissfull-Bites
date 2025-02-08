from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    thumbnail_image = models.ImageField(upload_to="categories/",max_length=300,null=True,default=None)
    description = models.CharField(max_length=250,null=True)

class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=300)
    quantity_desc = models.CharField(max_length=30,default="1pc")
    product_image = models.ImageField(upload_to="products/",max_length=300,null=True,default=None)

# Create your models here.