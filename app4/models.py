from django.db import models

# Create your models here.

class Customer(models.Model):
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
    CustomerName=models.CharField(max_length=30,null=True)     

class Expected(models.Model):
    estimatedprice=models.CharField(max_length=10)
    st=models.CharField(max_length=10) 
    et=models.CharField(max_length=10) 
    cuid=models.CharField(max_length=10) 

class liveValue(models.Model):
    name=models.CharField(max_length=100)
    bookingId=models.CharField(max_length=5,null=True)

class FinishedWorkList(models.Model):
    cuid=models.CharField(max_length=5)
    FinishedWork=models.CharField(max_length=50)
    ProductName=models.CharField(max_length=50)
    TimeTaken=models.CharField(max_length=10)
    Price=models.IntegerField(null=True,blank=True,default=1)