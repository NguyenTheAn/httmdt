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
from .views import *
from .an.views import *

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


]
