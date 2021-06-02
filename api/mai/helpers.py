import random
from ..models import *
import datetime
import numpy as np
from calendar import monthrange
from ..long.helpers import *

def getShoppingCart(customerid = None):
    carts = Shoppingcart.objects.filter(customerid__id = customerid)
    customer = Customer.objects.get(id = customerid)
    if len(carts) == 0:
        cart = Shoppingcart()
        cart.customerid = customer
        cart.save()
    else:
        cart = Shoppingcart.objects.get(customerid__id = customerid)
    cartlines = [cartline for cartline in Cartline.objects.all()]
    return_data = []
    for cartline in cartlines:
        if cartline.shoppingcartid == cart.id:
            tmp = {}
            tmp["cartline_id"] = cartline.id
            tmp['item_id'] = cartline.item.id
            tmp["item"] = Item.objects.get(id = cartline.item.id).name
            tmp["price"] = Item.objects.get(id = cartline.item.id).price
            tmp["number"] = Item.objects.get(id = cartline.item.id).num
            return_data.append(tmp)
    return return_data

def getShippingAddressList(customerid = None):
    adds = Shippingaddress.objects.filter(customerid__id = customerid)
    return_data = []
    for add in adds:
        tmp = {}
        tmp["addresd_id"] = add.id
        tmp["name"] = add.name
        tmp["phone"] = add.phone
        tmp["address"] = add.add
        return_data.append(tmp)
    return return_data


def getCustomer(customerid=None):
    if customerid is not None:
        customer = Customer.objects.get(id=customerid)
        return {"customerid": customer.id,
                "userid": getUser(customer.userid.id)}
    else:  
        return [{"customerid": customer.id,
                 "userid": getUser(customer.userid.id)} for customer in Customer.objects.all()]


def getUser(userid = None):
    users = [user for user in User.objects.all()]
    role = np.array(["Customer", "WarehouseStaff", "SalesStaff", "OrderProcessStaff", "BusinessStaff"])
    return_data = []
    for user in users:
        list1 = np.array([Customer.objects.filter(userid=user.id).count(), Warehousestaff.objects.filter(userid=user.id).count(),
                    Salesstaff.objects.filter(userid=user.id).count(), Orderprocessstaff.objects.filter(userid=user.id).count(), 
                    Businessstaff.objects.filter(userid=user.id).count()])
        role_type = role[list1 != 0][0]
        tmp = {}
        tmp["user_id"] = user.id
        # tmp["username"] = Account.objects.get(userid=user.id).username
        # tmp["password"] = Account.objects.get(userid=user.id).password
        tmp["email"] = Contactinfo.objects.get(id=user.contactinfo.id).email
        #tmp["address"] = Address.objects.get(userid=user.id).town
        tmp["name"] = Fullname.objects.get(id=user.fullname.id).firstname
        tmp["type"] = role_type
        if role_type == "Customer":
            customer_id = Customer.objects.get(userid = user.id).id
            tmp["customer_id"] = customer_id
            tmp['cart'] = getShoppingCart(customerid = customer_id)
            
        if userid == user.id:
            return_data = tmp
            break
        return_data.append(tmp)
    return return_data

def getItemByCategory(itemid = None, category = None):
    # items = [item for item in Item.objects.all()]
    # type_list = np.array(["Book", "Clothes", "Electronic"])
    # return_data = []
    # book_data = []
    # clothes_data = []
    # electronic_data = []
    # for item in items:
    #     list1 = np.array([Book.objects.filter(productid=item.productid).count(), Clothes.objects.filter(productid=item.productid).count(),
    #                 Electronic.objects.filter(productid=item.productid).count()])
    #     type = type_list[list1 != 0][0]
    #     tmp = {}
    #     tmp["id"] = item.id
    #     # tmp["name"] = item.name
    #     tmp["price"] = item.price
    #     tmp["des"] = item.description
    #     tmp["type"] = type
    #     if type == "Book":
    #         book_data.append(tmp)
    #     elif type == "Clothes":
    #         clothes_data.append(tmp)
    #     elif type == "Electronic":
    #         electronic_data.append(tmp)
    #     elif itemid == item.id:
    #         return_data = tmp
    #         break
    #     else:
    #         return_data.append(tmp)
    # if category == "Book":
    #     return book_data
    # elif category == "Clothes":
    #     return clothes_data
    # elif category == "Electronic":
    #     return electronic_data
    # return return_data

    if category.lower() == 'book':
        items = [item for item in Item.objects.filter(productid__categoryid__name='book')]
        return [getItem(item.id) for item in items]
    if category.lower() == 'clothes':
        items = [item for item in Item.objects.filter(productid__categoryid__name='clothes')]
        return [getItem(item.id) for item in items]
    if category.lower() == 'electronic':
        items = [item for item in Item.objects.filter(productid__categoryid__name='electronic')]
        return [getItem(item.id) for item in items]
