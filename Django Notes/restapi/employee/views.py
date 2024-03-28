from django.shortcuts import render
from rest_framework import viewsets
from employee.models import Employee
from employee.serializers import EmployeeSerializer

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
   queryset=Employee.objects.all()
   serializer_class = EmployeeSerializer