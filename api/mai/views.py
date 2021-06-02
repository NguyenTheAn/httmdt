import re
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from ..models import *
from ..helpers.common import *
import datetime
import numpy as np
from .helpers import *

class Register(APIView):
    def post(self, request, format=None):
        data = request.data
        accounts = [account for account in Account.objects.all()]
        usernames = [account.username for account in accounts]
        
        if data["email"] in usernames:
            return json_format(code = 400, message = "Account exists")

        address = Address()
        address.save()
        fullname = Fullname()
        fullname.firstname = data["name"]
        fullname.save()
        contactinfo = Contactinfo()
        contactinfo.email = data["email"]
        contactinfo.save()
        account = Account()
        account.username = data["email"]
        account.password = data["password"]
        account.save()
        user = User()
        user.account = account
        user.fullname = fullname
        user.contactinfo = contactinfo
        user.address = address

        user.save()

        if data["role"] == "Customer":
            a = Customer()
            a.userid = user
            a.save()
        elif data['role'] == "WarehouseStaff":
            a = Warehousestaff(userid = user)
            a.save()
        elif data['role'] == "SalesStaff":
            a = Salesstaff(userid = user)
            a.save()
        elif data['role'] == "OrderProcessStaff":
            a = Orderprocessstaff(userid = user)
            a.save()
        elif data['role'] == "BusinessStaff":
            a = Businessstaff(userid = user)
            a.save()
    
        return json_format(code = 200, message = "Success")

class Signin(APIView):
    
    def post(self, request, format=None):
        users = [user for user in User.objects.all()]
        accounts = [account for account in Account.objects.all()]
        data = request.data
        for user in users:
            for account in accounts:
                if user.account == account:
                    if account.username == data["username"] and account.password == data["password"]:
                        data1 = getUser(user.id)
                        return json_format(code = 200, message = "Login successfully", data = data1)
        return json_format(code = 400, message = "Wrong username or password")

class GetItemByCategory(APIView):
    def post(self, request, format=None):
        data = request.data
        data = getItem(category =  data["category"])
        return json_format(code = 200, message = "Success", data = data)    

class GetItemDetail(APIView):

    def post(self, request, format = None):
        data = request.data
        data = getItem(itemid = data["item_id"])
        return json_format(code = 200, message= "Success", data = data)

class GetAllItem(APIView):

    def post(self, request, format =  None):
        data = request.data
        data = getItem()
        return json_format(code=200, message="Success", data = data)

class GetShippingAddress(APIView):

    def post(self, request, format = None):
        data = request.data
        data = getShippingAddressList(customerid=data["customer_id"])
        return json_format(code = 200, message= "Success", data = data)

class AddShippingAddress(APIView):

    def post(self, request, format = None):
        data = request.data
        shippingaddress = Shippingaddress()
        shippingaddress.name = data["name"]
        shippingaddress.phone = data["phone"]
        shippingaddress.add = data["add"]
        shippingaddress.save()
        return json_format(code = 200, message= "Success")

