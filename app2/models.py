from django.db import models

# Create your models here.

class addemployees(models.Model):
    employeefullname=models.CharField(max_length=20)
    employeeplace=models.CharField(max_length=20)
    employeephonenumber=models.BigIntegerField()
    employeeemail=models.CharField(max_length=20)
    employeepassword=models.CharField(max_length=10)
    salary=models.BigIntegerField(null=True)
 
class addworkshop(models.Model):
    workshopname=models.CharField(max_length=20)
    workshopplace=models.CharField(max_length=20)
    phonenumber=models.BigIntegerField()
    workshopemail=models.CharField(max_length=20)
    workshoppassword=models.CharField(max_length=10)

class deletedworkshop(models.Model):
    workshopname=models.CharField(max_length=20)
    workshopplace=models.CharField(max_length=20)
    phonenumber=models.BigIntegerField()
    workshopemail=models.CharField(max_length=20)
    workshoppassword=models.CharField(max_length=10)

class deletedemployees(models.Model):
    employeefullname=models.CharField(max_length=20)
    employeeplace=models.CharField(max_length=20)
    employeephonenumber=models.BigIntegerField()
    employeeemail=models.CharField(max_length=20)
    employeepassword=models.CharField(max_length=10)
    salary=models.BigIntegerField(null=True)

class addwaterservice(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    phonenumber=models.BigIntegerField()
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=10)

class deletewaterservice(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    phonenumber=models.BigIntegerField()
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    



    
