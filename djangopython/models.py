from django.db import models

# Create your models here.

class Salesperson(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharFild(max_length=50)

class SalesInvoice(models.Model):
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


class Service(models.Model):
    service_Name = models.CharFild(max_length=50)
    hourly_Rate = models.IntField(max_length=50)



 
