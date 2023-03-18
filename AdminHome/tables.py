import django_tables2 as tables
from .models import Customer,Employee

class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        #template_name = "django_table2/bootstrap.html"
        fields = {"name","email","phone","address"}

class EmployeesTable(tables.Table):
    class Meta:
        model = Employee
        fields = {"Name","email","role","salary"}

class ProductTable(tables.Table):
    class Meta:
        model = Employee
        fields = {"Name","price","description","date_created"}