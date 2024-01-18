from django.shortcuts import render
from myapp.forms import EmployeeForm
from django.http import HttpResponse
from django import forms
from django.core.exceptions import ValidationError

# Create your views here.
def show_form(request):
   emp_form = EmployeeForm()
   if(request.method=="POST"):
      emp_form = EmployeeForm(request.POST)
      
      if(emp_form.is_valid()):
         print(emp_form.cleaned_data['name'])
         ename = emp_form.cleaned_data['name']
         #write a code to validate ename
         return HttpResponse("Form Submitted")
   return render(request,'employeeform.html',{'form':emp_form})
