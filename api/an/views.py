import re
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from ..models import *
from ..helpers.common import *
import datetime
import numpy as np
from .helpers import *

class AddItem2Cart(APIView):
    def post(self, request):
        data = request.data
        userid = data['userid']
        item = Item.objects.get(id = data['itemid'])
        customer = Customer.objects.get(userid__id = userid)
        if Shoppingcart.objects.filter(customerid__id = customer.id).count() == 0:
            cart = Shoppingcart(customerid = customer)
        else:
            cart = Shoppingcart.objects.get(customer__id = customer.id)

        if Cartline.objects.filter(shoppingcartid__id = cart.id, item__id = item.id).count() == 0:
            cartline = Cartline(shoppingcartid = cart, item = item, num = 1)
        else:
            cartline = Cartline.objects.get(shoppingcartid__id = cart.id, item__id = item.id)
            cartline.num += 1

        cart.save()
        cartline.save()

        return json_format(code=200, message="success", data = None)

class GetCart(APIView):
    def post(sef, request):
        data = request.data
        