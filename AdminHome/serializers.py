from rest_framework import serializers
from .models import Customer,Employee
 

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=150)
    phone = serializers.CharField(max_length=15)
    address=serializers.CharField(max_length=255)

    def create(self, validated_data):
        print("create methon called")
        return Customer.objects.create(**validated_data)
        
    def update(self, customer, validated_data):
        newCustomer = Customer(**validated_data)
        newCustomer.id = customer.id
        newCustomer.save()
        return newCustomer
 
class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=150)
    position = serializers.CharField(max_length=150)
    salary = serializers.FloatField()
    start_date=serializers.DateTimeField()

    # start_date=serializers.DateTimeField(auto_now=True)
    