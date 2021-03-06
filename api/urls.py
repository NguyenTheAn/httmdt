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
from .long.views import *
from .an.views import *
from .mai.views import *
from .views import *

urlpatterns = [
    # partner
    # path('AllTaxStatistic', AllTaxStatistic.as_view(), name = "AllTaxStatistic"), sample

    # Producer
    path('add_producer', AddProducer.as_view(), name = "add_producer"),
    path('get_producer', GetProducer.as_view(), name = "get_producer"),

    # Product
    path('add_product', AddProduct.as_view(), name = "add_product"),
    path('get_product', GetProduct.as_view(), name = "get_product"),
    path('edit_product', EditProduct.as_view(), name = "edit_product"),
    path('delete_product', DeleteProduct.as_view(), name = "delete_product"),

    # Import product
    path('import_product', ImportProduct.as_view(), name = "import_product"),

    # Item
    path('add_item', AddItem.as_view(), name = "add_item"),
    path('edit_item', EditItem.as_view(), name = "edit_item"),
    path('get_item', GetItem.as_view(), name = "get_item"),

    # Feedback
    path('add_feedback', AddFeedback.as_view(), name = "add_feedback"),
    path('get_feedback', GetFeedbackByItem.as_view(), name = "get_feedback"),

    path('register', Register.as_view(), name = "create_account"),
    path('signin', Signin.as_view(), name = "log_in"),
    path('get_item_by_category', GetItemByCategory.as_view(), name = "get_item_by_category"),
    path('get_all_item', GetAllItem.as_view(), name = "get_all_item"),
    # path('get_item_detail', GetItemDetail.as_view(), name = "get_item_detail"),
    path('get_shipping_address', GetShippingAddress.as_view(), name = "get_shipping_address"),
    path('add_shipping_address', AddShippingAddress.as_view(), name = "add_shipping_address"),
    path('add_item_to_cart', AddItem2Cart.as_view(), name = "AddItem2Cart"),
    path('get_shopping_cart', GetShoppingCart.as_view(), name = "GetShoppingCart"),
    path('add_order', AddOrder.as_view(), name = "add_order"),
    path('get_order_history', GetOrderHistory.as_view(), name = "get_order_history"),
    path('get_all_order', GetAllOrder.as_view(), name = "get_all_order"),
    path('confirm_order', ConfirmOrder.as_view(), name = "confirm_order"),
]
