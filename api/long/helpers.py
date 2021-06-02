from ..models import *

def addAddress(city,
               district,
               town,
               street,
               description):

    address = Address()
    address.city = city
    address.district = district
    address.town = town
    address.street = street
    address.description = description

    address.save()

    return address

def getAddress(addressid=None):
    if addressid is not None:
        address = Address.objects.get(id=addressid)
        return {"addressid": address.id,
                "city": address.city,
                "district": address.district,
                "town": address.town,
                "street": address.street,
                "description": address.description}
    
    else:
        return [{"addressid": address.id,
                "city": address.city,
                "district": address.district,
                "town": address.town,
                "street": address.street,
                "description": address.description} for address in Address.objects.all()]

def getProducer(producerid=None):

    if producerid is not None:
        producer = Producer.objects.get(id=producerid)
        return {"producerid": producer.id,
                "address": getAddress(producer.addressid.id),
                "name": producer.name,
                "phonenumber": producer.phonenumber,
                "email": producer.email}
    else:  
        return [{"producerid": producer.id,
                 "address": getAddress(producer.addressid.id),
                 "name": producer.name,
                 "phonenumber": producer.phonenumber,
                 "email": producer.email} for producer in Producer.objects.all()]

def addCategory(name, description=None):

    categories = [category for category in Category.objects.all()]
    for category in categories:
        if category.name == name:
            return category
            
    category = Category()
    category.name = name
    category.description = description
    category.save()

    return category

def addSuplier(name, phonenumber=None, email=None):

    suppliers = [suplier for suplier in Supplier.objects.all()]
    for suplier in suppliers:
        if suplier.name == name:
            return suplier
            
    suplier = Supplier()
    suplier.name = name
    suplier.phonenumber = phonenumber
    suplier.email = email
    suplier.save()

    return suplier

def getCategory(categoryid=None):
    if categoryid is not None:
        category = Category.objects.get(id=categoryid)
        return {"categoryid": category.id,
                "name": category.name,
                "description": category.description}
    
    else:
        return [{"categoryid": category.id,
                "name": category.name,
                "description": category.description} for category in Category.objects.all()]

def getProduct(productid=None):

    if productid is not None:
        product = Product.objects.get(id=productid)
        return {"productid": product.id,
                "producerid": getProducer(product.producerid.id),
                "categoryid": getCategory(product.categoryid.id),
                "manifacturingdate": product.manufacturingdate,
                "expirydate": product.expirydate,
                "amount": product.amount}
    else:  
        return [{"productid": product.id,
                "producerid": getProducer(product.producerid.id),
                "categoryid": getCategory(product.categoryid.id),
                "manifacturingdate": product.manufacturingdate,
                "expirydate": product.expirydate,
                "amount": product.amount} for product in Product.objects.all()]