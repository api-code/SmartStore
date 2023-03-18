from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from AdminHome.views import CustomerTableView,EmployeeListView,ProductListView,customerListView,employeeListView,customerDetailsView
urlpatterns = [
    path('',views.home,name='home'),
    path('signUp',views.signUp,name='signUp'),
    path('signin',views.signIn,name='signin'),
    path('signout',views.signOut,name='signout'),

    path('allCustomers',CustomerTableView.as_view(),name='allCustomers'), #its render the data using django table 
    path('SmartStore/customers',customerListView,name='SmartStore'), #its render the data using api,serializer
    path('SmartStore/customers/<int:pk>',customerDetailsView,name='SmartStore'), #its render the data using api,serializer

    path('Employees',EmployeeListView.as_view(),name='Employees'),#its render the data using django table 
    path('SmartStore/employees',employeeListView,name='SmartStore/employees'),

    path('products',ProductListView.as_view(),name='products'),

]
