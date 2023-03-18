from django.db import models
import datetime

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15)
    address=models.TextField()

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    salary = models.FloatField()
    start_date=models.DateTimeField(datetime.datetime)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    Name = models.CharField(max_length=150,null=True)
    price = models.FloatField(null=True)
    #category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    product_added_Date=models.DateTimeField(auto_now=True)
	#image=models.ImageField(upload_to ='static\images', default="")
    
    def __str__(self) -> str:
        return self.Name