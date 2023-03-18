from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django_tables2 import SingleTableView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from .models import Customer,Employee,Product
from .tables import CustomerTable,EmployeesTable,ProductTable
from .serializers import CustomerSerializer,EmployeeSerializer
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status


# Create your views here.
#@login_required(login_url='signin') #login decorator its indicated login is required for next page

#if user didnt have account then he/her will need to signup
#signUp is working
def signUp(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=UserCreationForm()
    
        if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username') #this gives us username withput any other info
                messages.success(request,user+" "+ 'your account has been create. you can log in now!')
                return redirect('signin')
            

    context={'form':form}
    return render(request,"AdminHome\signup.html",context)

#signin is working
def signIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user= authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'username or password is incorrect')

    context={}
    return render(request,"AdminHome\signin.html",context)

#its not working
def signOut(request):
    logout(request)
    return redirect(request,"AdminHome\signin.html")

#its working
def home(request):
    return render(request,"AdminHome\home.html")

# def allCustomers(request):
#     # if request.method == "POST":
#     #     name = request.POST.get('name')
#     #     email = request.POST.get('email')
#     #     phone = request.POST.get('phone')
#     #     address = request.POST.get('address')
#     Customer  = Customer.object.all()
#     return render(request,"AdminHome\AllCustomers.html",{'customer':Customer})

#customerlistview is working
@csrf_exempt
#non primary key based operation
def customerListView(request):
    #it gives all customer list
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer,many=True)
        print(serializer.data)
        #context={'serializer':serializer.data}
        #return render(request,'AdminHome\AllCustomers.html',context)
        return JsonResponse(serializer.data, safe=False)
    
    #this is function based view which save details of 1 customer
    elif request.method == 'POST':
        JsonData = JSONParser().parse(request)
        serializer = CustomerSerializer(data=JsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)
    
@csrf_exempt
def customerDetailsView(request,pk):
    try:
        customer = Customer.objects.get(pk=pk)
        # return JsonResponse("Customer" + str(pk), safe=False)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)
        
    

    if request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT':
        JsonData = JSONParser().parse(request)
        serializer = CustomerSerializer(customer ,data=JsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)



#Customer table view is working
class CustomerTableView(SingleTableView):
    model = Customer
    table_class = CustomerTable
    #queryset = Customer.objects.all()
    template_name = 'AdminHome\AllCustomers.html'

#employeelistview is working
class EmployeeListView(SingleTableView):
    model = Employee
    table_class = EmployeesTable 
    #queryset = Employee.objects.all()
    template_name = 'AdminHome\AllEmployees.html'

def employeeListView(request):
    employee = Employee.objects.all()
    # print(employee)
    # return JsonResponse({"employee":"proceess"})
    serializer = EmployeeSerializer(employee,many=True)
    print(serializer.data)
    return JsonResponse(serializer.data,safe=False)

#productlistview is also working
class ProductListView(SingleTableView):
    model = Product
    table_class = ProductTable 
    #queryset = Employee.objects.all()
    template_name = 'AdminHome\AllEmployees.html'


