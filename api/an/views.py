import re
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from ..models import *
from ..helpers.common import *
import datetime
import numpy as np
from .helpers import *
from ..mai.helpers import getShoppingCart

class AddItem2Cart(APIView):
    def post(self, request):
        data = request.data
        userid = data['userid']
        item = Item.objects.get(id = data['itemid'])
        customer = Customer.objects.get(userid__id = userid)
        if Shoppingcart.objects.filter(customerid__id = customer.id).count() == 0:
            cart = Shoppingcart(customerid = customer)
        else:
            cart = Shoppingcart.objects.get(customerid__id = customer.id)
            cart.save()

        if Cartline.objects.filter(shoppingcartid__id = cart.id, item__id = item.id).count() == 0:
            cartline = Cartline(shoppingcartid = cart, item = item, num = 1)
        else:
            cartline = Cartline.objects.get(shoppingcartid__id = cart.id, item__id = item.id)
            cartline.num += 1

        cartline.save()

        return json_format(code=200, message="success", data = None)

class GetShoppingCart(APIView):
    def post(self, request):
        data = request.data
        shoppingcart = getShoppingCart(data['customerid'])
        return json_format(code=200, message="success", data = shoppingcart)

class AddOrder(APIView):
    def post(self, request):
        data = request.data
        customerid = data['customerid']
        customer = Customer.objects.get(id = customerid)
        voucher = Voucher.objects.get(id = data['voucherid']) if "voucherid" in data.keys() else None
        shoppingcart = Shoppingcart.objects.get(customerid__id = customerid)
        shippingaddress = Shippingaddress.objects.get(id = data['shippingaddressid'])
        if Shippinginfo.objects.all().count() == 0:
            shippinginfo = Shippinginfo(shipfee = 15000, delaydate = 3)
            shippinginfo.save()
        else:
            shippinginfo = Shippinginfo.objects.get(id = 1)
        order= Order(orderprocessstaffuserid = None, customeruserid = customer, voucherid = voucher, shoppingcartid = shoppingcart, shippingaddress = shippingaddress, shippinginfo = shippinginfo, status = "Not Confirm")
        order.save()
        orderhistory = Orderhistory.objects.get(customerid__id = customerid)
        orderline = Historyline(orderhistoryid = orderhistory, orderinfo = order)
        orderline.save()
        
        return json_format(code=200, message="success", data = None)

class GetOrderHistory(APIView):
    def post(self, request):
        data = request.data
        customerid = data['customerid']
        orderlines = getOrderline(customerid)

        return json_format(code=200, message="success", data = orderlines)

class GetAllOrder(APIView):
    def get(self, request):
        order = getOrder()
        return json_format(code=200, message="success", data = order)

class ConfirmOrder(APIView):
    def post(self, request):
        data = request.data
        staffid = Orderprocessstaff.objects.get(id = data['staffid'])
        order = Order.objects.get(id = data['orderid'])
        order.orderprocessstaffuserid = staffid
        order.status = "Confirmed"
        order.save()

        return json_format(code=200, message="success", data = None)