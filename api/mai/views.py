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
        
        if data["username"] in usernames:
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
        user.fullname = fullname.id
        user.contactinfo = contactinfo.id
        user.address = address.id

        user.save()

        if data['role'] == "Customer":
            a = Customer(userid = user)
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