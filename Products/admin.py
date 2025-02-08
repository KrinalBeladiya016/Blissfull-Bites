from django.contrib import admin
from Products.models import Category
from Products.models import Product

class ManageProducts(admin.ModelAdmin):
    list_display = ('name','price','category','description','product_image')

admin.site.register(Product,ManageProducts)

class ManageCategories(admin.ModelAdmin):
    list_display = ('name','thumbnail_image')

admin.site.register(Category,ManageCategories)

# Register your models here.
