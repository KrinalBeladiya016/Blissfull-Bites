from django.contrib import admin
from User.models import *
class manageUsers(admin.ModelAdmin):
    list_display = ('name','email','contact_no','password','address')

admin.site.register(userDetails,manageUsers)

# class ManageOrders(admin.ModelAdmin):
#     list_display = ('email','productId','quantity')

# admin.site.register(OrderDetails,ManageOrders)

class ManageOrders(admin.ModelAdmin):
    list_display = ('id','email','total_amount','order_time')

admin.site.register(User_Orders,ManageOrders)

class ManageProductOrders(admin.ModelAdmin):
    list_display = ('order_id','product_id','quantity')

admin.site.register(Order_Products,ManageProductOrders)

class ManageFranchise(admin.ModelAdmin):
    list_display = ('name','email','contact_no','state','city','pincode')

admin.site.register(Franchise,ManageFranchise)
# Register your models here.
