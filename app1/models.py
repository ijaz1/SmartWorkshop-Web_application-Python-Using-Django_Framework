from django.db import models

from app2.models import addworkshop

# Create your models here.

class signuptb(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phonenumber=models.BigIntegerField()
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=10)

class workshopnames(models.Model):
    wsname=models.ForeignKey(addworkshop,on_delete=models.CASCADE)


