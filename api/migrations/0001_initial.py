# Generated by Django 3.0.5 on 2021-06-03 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='Username', max_length=255, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=255, null=True)),
                ('role', models.CharField(blank=True, db_column='Role', max_length=255, null=True)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, db_column='City', max_length=255, null=True)),
                ('district', models.CharField(blank=True, db_column='District', max_length=255, null=True)),
                ('town', models.CharField(blank=True, db_column='Town', max_length=255, null=True)),
                ('street', models.CharField(blank=True, db_column='Street', max_length=255, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Contactinfo',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=255, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
            ],
            options={
                'db_table': 'contactinfo',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Fullname',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=255, null=True)),
                ('middlename', models.CharField(blank=True, db_column='MiddleName', max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=255, null=True)),
            ],
            options={
                'db_table': 'fullname',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=255, null=True)),
                ('customeruserid', models.ForeignKey(db_column='CustomerUserID', on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('amount', models.IntegerField(blank=True, db_column='Amount', null=True)),
                ('method', models.CharField(blank=True, db_column='Method', max_length=255, null=True)),
                ('orderid', models.ForeignKey(db_column='OrderID', on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=255, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
                ('addressid', models.OneToOneField(db_column='AddressID', on_delete=django.db.models.deletion.CASCADE, to='api.Address')),
            ],
            options={
                'db_table': 'producer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('manufacturingdate', models.DateField(blank=True, db_column='ManufacturingDate', null=True)),
                ('expirydate', models.DateField(blank=True, db_column='ExpiryDate', null=True)),
                ('amount', models.IntegerField(blank=True, db_column='Amount', null=True)),
                ('categoryid', models.ForeignKey(db_column='CategoryID', on_delete=django.db.models.deletion.CASCADE, to='api.Category')),
                ('producerid', models.ForeignKey(db_column='ProducerID', on_delete=django.db.models.deletion.CASCADE, to='api.Producer')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Shippinginfo',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('shipfee', models.FloatField(blank=True, db_column='ShipFee', null=True)),
                ('delaydate', models.IntegerField(blank=True, db_column='DelayDate', null=True)),
                ('note', models.CharField(blank=True, db_column='Note', max_length=255, null=True)),
            ],
            options={
                'db_table': 'shippinginfo',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=255, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, db_column='Content', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tax',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('dateofbirth', models.DateField(blank=True, db_column='DateOfBirth', null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=255, null=True)),
                ('account', models.ForeignKey(db_column='AccountID', on_delete=django.db.models.deletion.CASCADE, to='api.Account')),
                ('address', models.ForeignKey(db_column='AddressID', on_delete=django.db.models.deletion.CASCADE, to='api.Address')),
                ('contactinfo', models.ForeignKey(db_column='ContactinfoID', on_delete=django.db.models.deletion.CASCADE, to='api.Contactinfo')),
                ('fullname', models.ForeignKey(db_column='FullnameID', on_delete=django.db.models.deletion.CASCADE, to='api.Fullname')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('discountpercent', models.FloatField(blank=True, db_column='DiscountPercent', null=True)),
                ('maxamount', models.IntegerField(blank=True, db_column='MaxAmount', null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
            ],
            options={
                'db_table': 'voucher',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('cardnumber', models.CharField(blank=True, db_column='CardNumber', max_length=255, null=True)),
                ('bank', models.CharField(blank=True, db_column='Bank', max_length=255, null=True)),
                ('paymentid', models.OneToOneField(db_column='PaymentID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Payment')),
            ],
            options={
                'db_table': 'card',
            },
        ),
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('paymentid', models.OneToOneField(db_column='PaymentID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Payment')),
            ],
            options={
                'db_table': 'cash',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('clothtype', models.CharField(blank=True, db_column='ClothType', max_length=255, null=True)),
                ('color', models.CharField(blank=True, db_column='Color', max_length=255, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=255, null=True)),
                ('ages', models.IntegerField(blank=True, db_column='Ages', null=True)),
                ('brand', models.CharField(blank=True, db_column='Brand', max_length=255, null=True)),
                ('material', models.CharField(blank=True, db_column='Material', max_length=255, null=True)),
                ('productid', models.OneToOneField(db_column='ProductID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Product')),
            ],
            options={
                'db_table': 'clothes',
            },
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('devicetype', models.CharField(blank=True, db_column='DeviceType', max_length=255, null=True)),
                ('color', models.CharField(blank=True, db_column='Color', max_length=255, null=True)),
                ('brand', models.CharField(blank=True, db_column='Brand', max_length=255, null=True)),
                ('material', models.CharField(blank=True, db_column='Material', max_length=255, null=True)),
                ('power', models.CharField(blank=True, db_column='Power', max_length=255, null=True)),
                ('voltage', models.CharField(blank=True, db_column='Voltage', max_length=255, null=True)),
                ('electriccurrent', models.CharField(blank=True, db_column='ElectricCurrent', max_length=255, null=True)),
                ('frequency', models.CharField(blank=True, db_column='Frequency', max_length=255, null=True)),
                ('productid', models.OneToOneField(db_column='ProductID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Product')),
            ],
            options={
                'db_table': 'electronic',
            },
        ),
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('paymentid', models.OneToOneField(db_column='PaymentID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Payment')),
            ],
            options={
                'db_table': 'qrcode',
            },
        ),
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('position', models.CharField(blank=True, db_column='Position', max_length=255, null=True)),
                ('salary', models.BigIntegerField(blank=True, db_column='Salary', null=True)),
                ('startdate', models.DateField(blank=True, db_column='StartDate', null=True)),
                ('workingtime', models.IntegerField(blank=True, db_column='WorkingTime', null=True)),
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.User')),
            ],
            options={
                'db_table': 'staffs',
            },
        ),
        migrations.CreateModel(
            name='Warehousestaff',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
            options={
                'db_table': 'warehousestaff',
            },
        ),
        migrations.CreateModel(
            name='Shoppingcart',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('customerid', models.ForeignKey(db_column='CustomerID', on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
            options={
                'db_table': 'shoppingcart',
            },
        ),
        migrations.CreateModel(
            name='Shippingaddress',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=255, null=True)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('add', models.CharField(blank=True, db_column='Add', max_length=255, null=True)),
                ('customerid', models.ForeignKey(db_column='CustomerID', on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
            options={
                'db_table': 'shippingaddress',
            },
        ),
        migrations.CreateModel(
            name='Salesstaff',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
            options={
                'db_table': 'salesstaff',
            },
        ),
        migrations.CreateModel(
            name='Orderprocessstaff',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
            options={
                'db_table': 'orderprocessstaff',
            },
        ),
        migrations.CreateModel(
            name='Orderhistory',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, db_column='Note', max_length=255, null=True)),
                ('customerid', models.ForeignKey(db_column='CustomerID', on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
            options={
                'db_table': 'orderhistory',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='orderprocessstaffuserid',
            field=models.ForeignKey(blank=True, db_column='OrderProcessStaffUserID', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Orderprocessstaff'),
        ),
        migrations.AddField(
            model_name='order',
            name='shippingaddress',
            field=models.ForeignKey(db_column='ShippingAddressID', on_delete=django.db.models.deletion.CASCADE, to='api.Shippingaddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='shippinginfo',
            field=models.ForeignKey(db_column='Shippinginfo', on_delete=django.db.models.deletion.CASCADE, to='api.Shippinginfo'),
        ),
        migrations.AddField(
            model_name='order',
            name='shoppingcartid',
            field=models.ForeignKey(db_column='ShoppingcartID', on_delete=django.db.models.deletion.CASCADE, to='api.Shoppingcart'),
        ),
        migrations.AddField(
            model_name='order',
            name='voucherid',
            field=models.ForeignKey(blank=True, db_column='VoucherID', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Voucher'),
        ),
        migrations.CreateModel(
            name='Membershiptype',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
                ('condition', models.CharField(blank=True, db_column='Condition', max_length=255, null=True)),
                ('customerid', models.ForeignKey(db_column='CustomerID', on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
            options={
                'db_table': 'membershiptype',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('price', models.BigIntegerField(blank=True, db_column='Price', null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
                ('productid', models.ForeignKey(db_column='ProductID', on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='Importingrecord',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, db_column='Date', null=True)),
                ('supplierid', models.ForeignKey(db_column='SupplierID', on_delete=django.db.models.deletion.CASCADE, to='api.Supplier')),
                ('warehousestaffuserid', models.ForeignKey(db_column='WarehouseStaffUserID', on_delete=django.db.models.deletion.CASCADE, to='api.Warehousestaff')),
            ],
            options={
                'db_table': 'importingrecord',
            },
        ),
        migrations.CreateModel(
            name='Importingline',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('amount', models.IntegerField(blank=True, db_column='Amount', null=True)),
                ('importprice', models.FloatField(db_column='ImportPrice')),
                ('importingrecordid', models.ForeignKey(db_column='ImportingrecordID', on_delete=django.db.models.deletion.CASCADE, to='api.Importingrecord')),
                ('productid', models.ForeignKey(db_column='ProductID', on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
            ],
            options={
                'db_table': 'importingline',
            },
        ),
        migrations.CreateModel(
            name='Historyline',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('orderhistoryid', models.ForeignKey(db_column='OrderHistoryID', on_delete=django.db.models.deletion.CASCADE, to='api.Orderhistory')),
                ('orderinfo', models.ForeignKey(db_column='OrderID', on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
            options={
                'db_table': 'historyline',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('rate', models.CharField(blank=True, db_column='Rate', max_length=255, null=True)),
                ('content', models.CharField(blank=True, db_column='Content', max_length=255, null=True)),
                ('customerid', models.ForeignKey(db_column='CustomerID', on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
                ('itemid', models.ForeignKey(db_column='ItemID', on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='Customerreview',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, db_column='Content', max_length=255, null=True)),
                ('reviewtime', models.DateField(blank=True, db_column='ReviewTime', null=True)),
                ('customerid', models.ForeignKey(db_column='CustomerID', on_delete=django.db.models.deletion.CASCADE, to='api.Customer')),
            ],
            options={
                'db_table': 'customerreview',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='userid',
            field=models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, to='api.User'),
        ),
        migrations.CreateModel(
            name='Cartline',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('num', models.IntegerField(blank=True, db_column='NumInCart', null=True)),
                ('item', models.ForeignKey(db_column='ItemID', on_delete=django.db.models.deletion.CASCADE, to='api.Item')),
                ('shoppingcartid', models.ForeignKey(db_column='ShoppingCartID', on_delete=django.db.models.deletion.CASCADE, to='api.Shoppingcart')),
            ],
            options={
                'db_table': 'cartline',
            },
        ),
        migrations.CreateModel(
            name='Businessstaff',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
            options={
                'db_table': 'businessstaff',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('page', models.IntegerField(blank=True, db_column='Page', null=True)),
                ('productid', models.OneToOneField(db_column='ProductID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api.Product')),
                ('author', models.ForeignKey(db_column='AuthorFullname', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Fullname')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
