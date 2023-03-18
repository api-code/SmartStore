from django.contrib import admin
from AdminHome.models import Customer
from AdminHome.models import Employee
from AdminHome.models import Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Product)
