from django.db import models

# Create your models here.

class fullServiceBooking(models.Model):
    BrandName=models.CharField(max_length=50)
    ModelName=models.CharField(max_length=50)
    ManufacturedYear=models.CharField(max_length=10)
    Purpose=models.CharField(max_length=20)
    Contact=models.CharField(max_length=12)
    OtherComplaints=models.CharField(max_length=300)
    Address=models.CharField(max_length=200)
    zip=models.CharField(max_length=10)
    WorkshopId=models.CharField(max_length=8)
    DateAndTime=models.CharField(max_length=60)
    clid=models.CharField(max_length=8,null=True)
    email=models.CharField(max_length=30,null=True)

class waterServBooking(models.Model):
    vehicle=models.CharField(max_length=10)
    cartype=models.CharField(max_length=11)
    servtype=models.CharField(max_length=20)
    watershopid=models.CharField(max_length=12)
    contact=models.CharField(max_length=12,null=True)
    ocomplaint=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    zip=models.CharField(max_length=10)
    watershopid=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    clientid=models.CharField(max_length=10)
    DateAndTime=models.CharField(max_length=60)
