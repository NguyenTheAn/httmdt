
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import *
from .helpers import *
from ..helpers.common import *
import datetime

class AddProducer(APIView):
    def post(self, request, format=None):
        data = request.data
        
        producer = Producer()

        address = addAddress(city=data['address_city'],
                             district=data['address_district'],
                             town=data['address_town'],
                             street=data['address_street'],
                             description=data['address_description'])
        
        producer.addressid = address
        producer.name = data['name']
        producer.phonenumber = data['phonenumber']
        producer.email = data['email']

        producer.save()

        return json_format(code = 200, message = "Success")

class GetProducer(APIView):
    def post(self, request, format=None):
        data = request.data
        
        return_data = getProducer()

        return json_format(code = 200, message = "Success", data=return_data)

class AddProduct(APIView):
    def post(self, request, format=None):
        data = request.data
        
        product = Product()

        producer = Producer.objects.get(id=data['producerid'])
        product.producerid = producer
        
        category = addCategory(data['category_name'],
                               data['category_description'])
        product.categoryid = category
        product.manufacturingdate = datetime.datetime.strptime(data['manufacturingdate'], "%d/%m/%Y")
        product.expirydate = datetime.datetime.strptime(data['expirydate'], "%d/%m/%Y")
        product.save()

        return json_format(code = 200, message = "Success")

class GetProduct(APIView):
    def post(self, request, format=None):
        data = request.data
        
        return_data = getProduct()

        return json_format(code = 200, message = "Success", data=return_data)