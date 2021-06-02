import random
from ..models import *
import datetime
import numpy as np
from calendar import monthrange

def getShoppingCart(customerid = None):
    cart = Shoppingcart.objects.get(customerid = customerid)
    cartlines = [cartline for cartline in Cartline.objects.all()]
    return_data = []
    for cartline in cartlines:
        if cartline.shoppingcartid == cart.id:
            tmp = {}
            tmp["carline_id"] = cartline.id
            tmp['item_id'] = cartline.item
            tmp["item"] = Item.objects.get(id = cartline.item).name
            tmp["price"] = Item.objects.get(id = cartline.item).price
            tmp["number"] = Item.objects.get(id = cartline.item).num
            return_data.append(tmp)
    return return_data

def getShippingAddressList(customerid = None):
    adds = [add for add in Shippingaddress.objects.all()]
    return_data = []
    for add in adds:
        if add.customerid == customerid:
            tmp = {}
            tmp["addresd_id"] = add.id
            tmp["name"] = add.name
            tmp["phone"] = add.phone
            tmp["add"] = add.note
            return_data.append(tmp)
    return return_data




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
        tmp["username"] = Account.objects.get(userid=user.id).username
        tmp["password"] = Account.objects.get(userid=user.id).password
        tmp["email"] = Contactinfo.objects.get(userid=user.id).email
        #tmp["address"] = Address.objects.get(userid=user.id).town
        tmp["name"] = Fullname.objects.get(userid=user.id).firstname
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

def getItem(itemid = None, category = None):
    items = [item for item in Item.objects.all()]
    type_list = np.array(["Book", "Clothes", "Electronic"])
    return_data = []
    book_data = []
    clothes_data = []
    electronic_data = []
    for item in items:
        list1 = np.array([Book.objects.filter(productid=item.productid).count(), Clothes.objects.filter(productid=item.productid).count(),
                    Electronic.objects.filter(productid=item.productid).count()])
        type = type_list[list1 != 0][0]
        tmp = {}
        tmp["id"] = item.id
        tmp["name"] = item.name
        tmp["price"] = item.price
        tmp["des"] = item.description
        tmp["type"] = role_type
        if type == "Book":
            book_data.append(tmp)
        elif type == "Clothes":
            clothes_data.append(tmp)
        elif type == "Electronic":
            electronic_data.append(tmp)
        if itemid == item.id:
            return_data = tmp
            break
    if category == "Book":
        return book_data
    elif category == "Clothes":
        return clothes_data
    elif category == "Electronic":
        return electronic_data
    return return_data