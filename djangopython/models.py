from django.db import models

# Create your models here.

class Salesperson(models.Model):
    salesperson_ID = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharFild(max_length=50)

class SalesInvoice(models.Model):
    invoice_ID = models.IntegerField(primary_key=True)
    invoice_number = models.IntegerField(max_length=50)
    date = models.DateTimeField("date invoiced")
    customer_id = models.IntegerField(max_length=50)
    salesperson_id = models.IntegerField(max_length=50)
    Car = models.ForeignKey(Car)
    Customer = models.ForeignKey(Customer)
    Salesperson = models.ForeignKey(Salesperson)
    
class Car(models.Model):
    car_ID = models.IntegerField(primary_key=True)
    serial_number = models.IntField(max_length=50)
    make = models.CharFild(max_length=50)
    model = models.CharFild(max_length=50)
    colour = models.CharFild(max_length=50)
    year = models.IntegerFild(max_length=50)
    car_For_Sale = models.BooleanFild(max_length=50)

class Customer(models.Model):
    customer_ID = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharFild(max_length=50)
    phone_Number = models.IntegerField(max_length=50)
    address = models.CharFild(max_length=100)
    city = models.CharFild(max_length=50)
    state_Province = models.CharFild(max_length=100)
    postalCode = models.IntgerFild(max_length=50)

class Service(models.Model):
    service_ID = models.IntegerField(primary_key=True)
    service_Name = models.CharFild(max_length=50)
    hourly_Rate = models.IntField(max_length=50)

class Parts(models.Model):
    parts_ID = models.IntegerField(primary_key=True)
    part_Number = models.IntField(max_length=50)
    description = models.CharFild(max_length=50)
    purchase_Price = models.IntField(max_length=50)
    retail_Price = models.IntField(max_length=50)

class Mechanic(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharFild(max_length=50)


 
