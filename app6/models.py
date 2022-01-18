from django.db import models

# Create your models here.


class AcceptedwaterServ(models.Model):
    vehicle = models.CharField(max_length=10)
    cartype = models.CharField(max_length=11)
    servtype = models.CharField(max_length=20)
    contact = models.CharField(max_length=12)
    ocomplaint = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zip = models.CharField(max_length=10)
    watershopid = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    clientid = models.CharField(max_length=10)
    DateAndTime = models.CharField(max_length=60)

class LiveValueWater(models.Model):
    valuewater=models.CharField(max_length=200)
    bookingId=models.CharField(max_length=10)
