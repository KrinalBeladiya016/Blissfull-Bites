"""
URL configuration for blissfull_bites project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blissfull_bites import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name="indexPage"),
    path("home/", views.homePage, name="home"),
    path("register/", views.registerUser, name="register"),
    path("categories/", views.showCategories, name="categories"),
    path("products/<categoryName>", views.getProducts, name="productsPage"),
    path("productDetails/<int:pid>", views.showProductDetails),
    path("products/addToCart/<int:pid>", views.addToCart, name="addToCart"),
    path("productDetails/addToCart/<int:pid>", views.addToCart),
    path("UserCart/", views.displayCart, name="openCart"),
    path("placeOrder/", views.placeOrder, name="placeOrder"),
    path("UserCart/getUserDetails/", views.getUserDetails, name="fetchUserDetails"),
    path("logout/", views.logOut, name="logOut"),
    path("signout/", views.signOut, name="signOut"),
    path("editprofile/", views.editUserProfile, name="editProfile"),
    path("UserCart/updateCart/<str:data>", views.updateCart, name="updateCart"),
    path("UserCart/deleteitem/<int:itemId>", views.deleteCartItem, name="deleteCartItem"),
    path("aboutUs/", views.showAboutInfo, name="aboutUsPage"),
    path("franchise/", views.franchiseDetails, name="franchise"),
    path("outlets/", views.showOutlets, name="outletDetails"),
    path("OrderHistory/", views.getUserOrders, name="orderHistory"),
    path("OrderHistory/OrderDetails/<int:oid>",views.getorderDetails,name="orderDetails",)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
