from django.shortcuts import render,redirect
from employee.models import EmployeeTable
# Create your views here.
def show_employee(request):
   data={}
   all_employee=EmployeeTable.objects.all()
   data['employees']=all_employee
   return render(request,'employee/show_employee.html',context=data)


def add_employee(request):
   if request.method=='POST':
      emp_name=request.POST['name']
      emp_salary=request.POST['salary']
      emp_designation=request.POST['designation']
      
      employee=EmployeeTable.objects.create(name=emp_name,salary=emp_salary,designation=emp_designation)

      employee.save()

      return redirect('/employee/show')
   return render(request,'employee/add_employee.html')

def delete_employee(request,empid):
   employee=EmployeeTable.objects.get(id=empid)
   employee.delete()
   return redirect('/employee/show')

def update_employee(request,empid):
   data={}
   fetched_employee=EmployeeTable.objects.get(id=empid)
   print(fetched_employee.name)
   data['employee']=fetched_employee
   if request.method=='POST':
      emp_name=request.POST['name']
      emp_salary=request.POST['salary']
      emp_designation=request.POST['designation']
      employee=EmployeeTable.objects.filter(pk=empid)
      employee.update(name=emp_name,salary=emp_salary,designation=emp_designation)

      return redirect('/employee/show')
   return render(request,'employee/update_employee.html',context=data)
