"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from .mai.views import *

urlpatterns = [
    path('register', Register.as_view(), name = "create_account"),
    path('signin', Signin.as_view(), name = "log_in"),
    path('get_item_by_category', GetItemByCategory.as_view(), name = "get_item_by_category"),
    path('get_all_item', GetAllItem.as_view(), name = "get_all_item"),
    path('get_item_detail', GetItemDetail.as_view(), name = "get_item_detail"),
    path('get_shipping_address', GetShippingAddress.as_view(), name = "get_shipping_address"),
    path('add_shipping_address', AddShippingAddress.as_view(), name = "add_shipping_address"),
]
