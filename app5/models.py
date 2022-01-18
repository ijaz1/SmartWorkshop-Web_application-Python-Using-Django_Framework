from django.db import models

# Create your models here.

class advertisement(models.Model):
    photo=models.CharField(max_length=400)
    mainhead=models.CharField(max_length=40)
    fsubhead=models.CharField(max_length=50)
    ssubhead=models.CharField(max_length=40)

class aboutus(models.Model):
    abouttext=models.CharField(max_length=1000)

class cotactus(models.Model):
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    whatsapp=models.CharField(max_length=10)

class CustFeedback(models.Model):
    photo=models.CharField(max_length=200)

class addproduct(models.Model):
    photo=models.ImageField(upload_to="product")
    name=models.CharField(max_length=40)
    price=models.CharField(max_length=10)
    stock=models.CharField(max_length=20)

