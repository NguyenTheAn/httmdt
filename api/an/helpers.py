from ..models import *
from ..mai.helpers import getUser
from ..mai.helpers import getShoppingCart
def getVoucher(id = None):
    if id is None:
        vouchers = Voucher.objects.all()
        data = [{"voucherid" : voucher.id, 
                "name": voucher.name, "discountpercent": voucher.voucher,
                "maxamount" : voucher.maxamount, "description": voucher.description} for voucher in vouchers]
    else:
        voucher = Voucher.objects.get(id = id)
        data = [{"voucherid" : voucher.id, 
                "name": voucher.name, "discountpercent": voucher.discountpercent,
                "maxamount" : voucher.maxamount, "description": voucher.description}]
    return data

def getOrderline(customerid):
    orderhistory = Orderhistory.objects.get(customerid__id = customerid)
    historylines = Historyline.objects.filter(orderhistoryid__id = orderhistory.id)
    data = [{"id":line.id,
             "order" : getOrder(line.orderinfo.id)} for line in historylines]
    return data

def getOrder(orderid = None):
    if orderid is None:
        data = [{"id" : order.id,
                #  "orderprocessstaffuserid" : getUser(order.orderprocessstaffuserid.userid.id) if order.orderprocessstaffuserid is not None else None,
                 "customer" : getUser(order.customeruserid.userid.id),
                #  "voucher" : getVoucher(order.voucherid.id) if order.voucherid is not None else None,
                 "orderitem" : getShoppingCart(order.shoppingcartid.customerid.id),
                 "shippingadress" : getShippingAdress(order.shippingaddress.id, order.customeruserid.id),
                 "shippinginfo" : getShippinginfo(order.shippinginfo.id)['shipfee'],
                 "status" : order.status} for order in Order.objects.all()]
    else:
        order = Order.objects.get(id = orderid)
        data = [{"id" : order.id,
                #  "orderprocessstaffuserid" : getUser(order.orderprocessstaffuserid.userid.id) if order.orderprocessstaffuserid is not None else None,
                 "customer" : getUser(order.customeruserid.userid.id),
                #  "voucher" : getVoucher(order.voucherid.id) if order.voucherid is not None else None,
                 "orderitem" : getShoppingCart(order.shoppingcartid.customerid.id),
                 "shippingadress" : getShippingAdress(order.shippingaddress.id, order.customeruserid.id),
                 "shippinginfo" : getShippinginfo(order.shippinginfo.id)['shipfee'],
                 "status" : order.status}]
    return data

def getShippingAdress(id = None, customerid = None):
    if id is not None:
        shippingadress = Shippingaddress.objects.get(id = id)
        data = {"id" : shippingadress.id,
                "name" : shippingadress.name,
                "phone" : shippingadress.phone,
                "add" : shippingadress.add}
    else:
        data = [{"id" : shippingadress.id,
                "name" : shippingadress.name,
                "phone" : shippingadress.phone,
                "add" : shippingadress.add} for shippingadress in Shippingaddress.objects.filter(customerid__id = customerid)]
    return data

def getShippinginfo(id = None):
    if id is not None:
        shippinginfo = Shippinginfo.objects.get(id = id)
        data = {"id" : shippinginfo.id,
                "shipfee" : shippinginfo.shipfee,
                "delaydate" : shippinginfo.delaydate,
                "note" : shippinginfo.note}
    return data