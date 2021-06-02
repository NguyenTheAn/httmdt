
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
        product.amount = 0
        product.save()

        return json_format(code = 200, message = "Success")

class GetProduct(APIView):
    def post(self, request, format=None):
        data = request.data
        
        return_data = getProduct()

        return json_format(code = 200, message = "Success", data=return_data)

class EditProduct(APIView):
    def post(self, request, format=None):
        data = request.data
        
        product = Product.objects.get(id=data['productid'])
        if "producerid" in data.keys():
            producer = Producer.objects.get(id=data['producerid'])
            product.producerid = producer
        if "categoryid" in data.keys():
            category = Category.objects.get(id=data['categoryid'])
            product.categoryid = category
        if "manufacturingdate" in data.keys():
            product.manufacturingdate = datetime.datetime.strptime(data['manufacturingdate'], "%d/%m/%Y")
        if "expirydate" in data.keys():
            product.expirydate = datetime.datetime.strptime(data['expirydate'], "%d/%m/%Y")
        product.save()

        return json_format(code = 200, message = "Success")

class DeleteProduct(APIView):
    def post(self, request, format=None):
        data = request.data
        
        product = Product.objects.get(id=data['productid'])
        product.delete()

        return json_format(code = 200, message = "Success")

class ImportProduct(APIView):
    def post(self, request, format=None):
        data = request.data

        importingRecord = Importingrecord()
        # staff = Warehousestaff.objects.get(id=data['warehousestaffuserid'])
        # supplier = Supplier.objects.get(id=data['supplierid'])
        
        # importingRecord.warehousestaffuserid = staff
        # importingRecord.supplierid = supplier
        importingRecord.date = datetime.datetime.now()

        importingRecord.save()

        for item in data['import_product']:
            importingline = Importingline()

            importingline.amount = item['amount']
            importingline.importprice = item['importprice']
            product = Product.objects.get(id=item['productid'])
            product.amount += importingline.amount

            importingline.productid = product
            importingline.importingrecordid = importingRecord

            importingline.save()
            product.save()
        return json_format(code = 200, message = "Success")