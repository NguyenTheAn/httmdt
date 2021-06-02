# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserID')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'account'


class Address(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # producerid = models.ForeignKey('Producer', models.CASCADE, db_column='ProducerID')  # Field name made lowercase.
    # userid = models.ForeignKey('User', models.CASCADE, db_column='UserID')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    town = models.CharField(db_column='Town', max_length=255, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='Street', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'address'


class Book(models.Model):
    page = models.IntegerField(db_column='Page', blank=True, null=True)  # Field name made lowercase.
    author = models.ForeignKey('Fullname', models.CASCADE, db_column='AuthorFullname')   # Field name made lowercase.
    genre = models.IntegerField(db_column='Genre', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('Product', models.CASCADE, db_column='ProductID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'book'


class BookGenre(models.Model):
    bookproductid = models.OneToOneField(Book, models.CASCADE, db_column='BookProductID', primary_key=True)  # Field name made lowercase.
    genreid = models.ForeignKey('Genre', models.CASCADE, db_column='GenreID')  # Field name made lowercase.

    class Meta:
        
        db_table = 'book_genre'
        unique_together = (('bookproductid', 'genreid'),)


class Businessstaff(models.Model):
    userid = models.OneToOneField('User', models.CASCADE, db_column='UserID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'businessstaff'


class Card(models.Model):
    cardnumber = models.CharField(db_column='CardNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bank = models.CharField(db_column='Bank', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentid = models.OneToOneField('Payment', models.CASCADE, db_column='PaymentID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'card'


class Cartline(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    shoppingcartid = models.ForeignKey('Shoppingcart', models.CASCADE, db_column='ShoppingCartID')  # Field name made lowercase.
    item = models.ForeignKey('Item', models.CASCADE, db_column='ItemID')  # Field name made lowercase.
    num = models.IntegerField(db_column = "NumInCart", blank=True, null=True)

    class Meta:
        
        db_table = 'cartline'


class Cash(models.Model):
    paymentid = models.OneToOneField('Payment', models.CASCADE, db_column='PaymentID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'cash'


class Category(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'category'


class Clothes(models.Model):
    clothtype = models.CharField(db_column='ClothType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ages = models.IntegerField(db_column='Ages', blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=255, blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('Product', models.CASCADE, db_column='ProductID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'clothes'


class Contactinfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # userid = models.ForeignKey('User', models.CASCADE, db_column='UserID')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'contactinfo'


class Customer(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # shippingaddress = models.IntegerField(db_column='ShippingAddress', blank=True, null=True)  # Field name made lowercase.
    # orderhistory = models.IntegerField(db_column='OrderHistory', blank=True, null=True)  # Field name made lowercase.
    # membershiptype = models.IntegerField(db_column='Membershiptype', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.CASCADE, db_column='UserID')  # Field name made lowercase.

    class Meta:
        
        db_table = 'customer'
        unique_together = (('id', 'userid'),)


class Customerreview(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerID')  # Field name made lowercase.
    # customeruserid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerUserID')  # Field name made lowercase.
    # customer = models.IntegerField(db_column='Customer', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reviewtime = models.DateField(db_column='ReviewTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'customerreview'


class Electronic(models.Model):
    devicetype = models.CharField(db_column='DeviceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=255, blank=True, null=True)  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=255, blank=True, null=True)  # Field name made lowercase.
    power = models.CharField(db_column='Power', max_length=255, blank=True, null=True)  # Field name made lowercase.
    voltage = models.CharField(db_column='Voltage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    electriccurrent = models.CharField(db_column='ElectricCurrent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    frequency = models.CharField(db_column='Frequency', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productid = models.OneToOneField('Product', models.CASCADE, db_column='ProductID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'electronic'


class Feedback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey('Item', models.CASCADE, db_column='ItemID')  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerID')  # Field name made lowercase.
    # customeruserid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerUserID')  # Field name made lowercase.
    # item = models.CharField(db_column='Item', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # customername = models.CharField(db_column='CustomerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'feedback'


class Fullname(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # bookproductid = models.ForeignKey(Book, models.CASCADE, db_column='BookProductID')  # Field name made lowercase.
    # userid = models.ForeignKey('User', models.CASCADE, db_column='UserID')  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'fullname'


class Genre(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'genre'


class Historyline(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderhistoryid = models.ForeignKey('Orderhistory', models.CASCADE, db_column='OrderHistoryID')  # Field name made lowercase.
    orderinfo = models.CharField(db_column='OrderInfo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'historyline'


class Importingrecord(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    warehousestaffuserid = models.ForeignKey('Warehousestaff', models.CASCADE, db_column='WarehouseStaffUserID')  # Field name made lowercase.
    supplierid = models.ForeignKey('Supplier', models.CASCADE, db_column='SupplierID')  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    supplier = models.IntegerField(db_column='Supplier', blank=True, null=True)  # Field name made lowercase.
    productid =models.ForeignKey("Product", models.CASCADE, db_column='ProductID') # Field name made lowercase.
    warehousestaff = models.IntegerField(db_column='WarehouseStaff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'importingrecord'


class Item(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # cartlineid = models.ForeignKey(Cartline, models.CASCADE, db_column='CartLineID')  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.CASCADE, db_column='ProductID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.BigIntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # feedback = models.IntegerField(db_column='Feedback', blank=True, null=True)  # Field name made lowercase.
    # promotion = models.IntegerField(db_column='Promotion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'item'


class Membershiptype(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerID')  # Field name made lowercase.
    # customeruserid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerUserID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    condition = models.CharField(db_column='Condition', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'membershiptype'


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderprocessstaffuserid = models.ForeignKey('Orderprocessstaff', models.CASCADE, db_column='OrderProcessStaffUserID')  # Field name made lowercase.
    # customeruserid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerUserID')  # Field name made lowercase.
    taxid = models.ForeignKey('Tax', models.CASCADE, db_column='TaxID')  # Field name made lowercase.
    voucherid = models.ForeignKey('Voucher', models.CASCADE, db_column='VoucherID')  # Field name made lowercase.
    historylineid = models.ForeignKey(Historyline, models.CASCADE, db_column='HistoryLineID')  # Field name made lowercase.
    shoppingcartid = models.ForeignKey("Shoppingcart", models.CASCADE, db_column='ShoppingcartID')
    # customer = models.IntegerField(db_column='Customer', blank=True, null=True)  # Field name made lowercase.
    # processstaffid = models.IntegerField(db_column='ProcessStaffID', blank=True, null=True)  # Field name made lowercase.
    # payment = models.IntegerField(db_column='Payment', blank=True, null=True)  # Field name made lowercase.
    # item = models.IntegerField(db_column='Item', blank=True, null=True)  # Field name made lowercase.
    # voucher = models.IntegerField(db_column='Voucher', blank=True, null=True)  # Field name made lowercase.
    shippingaddress = models.ForeignKey("ShippingAddress", models.CASCADE, db_column='ShippingAddressID')   # Field name made lowercase.
    # shoppingcart = models.IntegerField(db_column='ShoppingCart', blank=True, null=True)  # Field name made lowercase.
    shippinginfo =models.ForeignKey("Shippinginfo", models.CASCADE, db_column='Shippinginfo')   # Field name made lowercase.

    class Meta:
        
        db_table = 'order'


class Orderhistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerID')  # Field name made lowercase.
    # customeruserid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerUserID')  # Field name made lowercase.
    # historyline = models.IntegerField(db_column='Historyline', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'orderhistory'


class Orderprocessstaff(models.Model):
    userid = models.OneToOneField('User', models.CASCADE, db_column='UserID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'orderprocessstaff'


class Payment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.CASCADE, db_column='OrderID')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(db_column='Method', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'payment'


class Producer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # productid = models.ForeignKey('Product', models.CASCADE, db_column='ProductID')  # Field name made lowercase.
    addressid = models.OneToOneField(Address, models.CASCADE, db_column='AddressID')
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'producer'


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # importingrecordid = models.ForeignKey(Importingrecord, models.CASCADE, db_column='ImportingRecordID')  # Field name made lowercase.
    producerid = models.ForeignKey(Producer, models.CASCADE, db_column='ProducerID')  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.CASCADE, db_column='CategoryID')  # Field name made lowercase.
    manufacturingdate = models.DateField(db_column='ManufacturingDate', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.DateField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.
    # producer = models.IntegerField(db_column='Producer', blank=True, null=True)  # Field name made lowercase.
    # category = models.IntegerField(db_column='Category', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'product'


class Promotion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    percent = models.FloatField(db_column='Percent')  # Field name made lowercase.
    expirydate = models.DateField(db_column='ExpiryDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'promotion'


class PromotionItem(models.Model):
    promotionid = models.OneToOneField(Promotion, models.CASCADE, db_column='PromotionID', primary_key=True)  # Field name made lowercase.
    itemid = models.ForeignKey(Item, models.CASCADE, db_column='ItemID')  # Field name made lowercase.

    class Meta:
        
        db_table = 'promotion_item'
        unique_together = (('promotionid', 'itemid'),)


class Qrcode(models.Model):
    paymentid = models.OneToOneField(Payment, models.CASCADE, db_column='PaymentID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'qrcode'


class Salesstaff(models.Model):
    userid = models.OneToOneField('User', models.CASCADE, db_column='UserID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'salesstaff'


class Shippingaddress(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # orderid = models.ForeignKey(Order, models.CASCADE, db_column='OrderID')  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerID')  # Field name made lowercase.
    # customeruserid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerUserID')  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'shippingaddress'


class Shippinginfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # orderid = models.ForeignKey(Order, models.CASCADE, db_column='OrderID')  # Field name made lowercase.
    shipfee = models.FloatField(db_column='ShipFee', blank=True, null=True)  # Field name made lowercase.
    delaydate = models.CharField(db_column='DelayDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'shippinginfo'


class Shoppingcart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.CASCADE, db_column='CustomerID')  # Field name made lowercase.
    # orderid = models.ForeignKey(Order, models.CASCADE, db_column='OrderID')  # Field name made lowercase.
    # cartline = models.IntegerField(db_column='CartLine', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'shoppingcart'


class Staffs(models.Model):
    position = models.CharField(db_column='Position', max_length=255, blank=True, null=True)  # Field name made lowercase.
    salary = models.BigIntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    workingtime = models.IntegerField(db_column='WorkingTime', blank=True, null=True)  # Field name made lowercase.
    userid = models.OneToOneField('User', models.CASCADE, db_column='UserID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'staffs'


class Supplier(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'supplier'


class Tax(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'tax'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dateofbirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # account = models.IntegerField(db_column='Account', blank=True, null=True)  # Field name made lowercase.
    addressid = models.OneToOneField(Address, models.CASCADE, db_column='AddressID')  # Field name made lowercase.
    # fullname = models.IntegerField(db_column='FullName', blank=True, null=True)  # Field name made lowercase.
    fullname = models.ForeignKey('FullName', models.CASCADE, db_column='FullName')
    contactinfo = models.ForeignKey('Contactinfo', models.CASCADE, db_column='Contactinfo')
    # contactinfo = models.IntegerField(db_column='Contactinfo', blank=True, null=True)  # Field name made lowercase.
    # address = models.IntegerField(db_column='Address', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'user'


class Voucher(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    discountpercent = models.FloatField(db_column='DiscountPercent', blank=True, null=True)  # Field name made lowercase.
    discountamount = models.IntegerField(db_column='DiscountAmount', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'voucher'


class Warehousestaff(models.Model):
    userid = models.OneToOneField(User, models.CASCADE, db_column='UserID', primary_key=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'warehousestaff'
