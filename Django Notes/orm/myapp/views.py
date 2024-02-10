from django.shortcuts import render
from myapp import models
from django.db.models import Q,Avg,Sum,Min,Max,Count

# Create your views here.
def view(request):
   #-----------getting all employees
   #employees=models.Employee.objects.all()
   #print(type(employees))  
   #<class 'django.db.models.query.QuerySet'>
   #print(employees)
   #<QuerySet [<Employee: Employee object (1)>, <Employee: Employee object (2)>, <Employee: Employee object (3)>, <Employee: Employee object (4)>, <Employee: Employee object (5)>]>
   # Queryset is list of object of model
   #print(employees.query)
   #SELECT `myapp_employee`.`id`, `myapp_employee`.`name`, `myapp_employee`.`salary`, `myapp_employee`.`city` FROM `myapp_employee`
   
   #---------------getting single employee based on id
   # employee=models.Employee.objects.get(id=1)
   # print(type(employee)) <class 'myapp.models.Employee'>
   
   #---------------getting single employee using filter
   #employees=models.Employee.objects.filter(id=1)
   #employees=models.Employee.objects.filter(id__in=[1,3])
   #print(type(employees)) 
   #<class 'django.db.models.query.QuerySet'>
   #print(employees) 
   #<QuerySet [<Employee: Employee object (1)>]>
   #print(employees.query)
   #SELECT `myapp_employee`.`id`, `myapp_employee`.`name`, `myapp_employee`.`salary`, `myapp_employee`.`city` FROM `myapp_employee` WHERE `myapp_employee`.`id` IN (1, 3)
   
   #-------------employees with salary >15000
   #employees=models.Employee.objects.filter(salary__gt=15000)
   
   #-------------employees with salary <15000
   #employees=models.Employee.objects.filter(salary__lt=15000)
   
   #----employees with salary >15000 and lives in delhi
   #employees=models.Employee.objects.filter(salary__gt=15000,city='delhi')
   
   #----employees with salary >15000 or lives in delhi
   #employees=models.Employee.objects.filter(Q(salary__gt=15000)|Q(city='delhi'))
   
   #----employees not lives in delhi
   #employees=models.Employee.objects.exclude(city='delhi')
   
   #----employees order by salary ascending
   #employees=models.Employee.objects.all().order_by('salary')
   
   #----employees order by salary descending
   #employees=models.Employee.objects.all().order_by('-salary')
   
   #----employees 2nd highest salary
   #employee=models.Employee.objects.all().order_by('salary')[1]
   
   #----employees order by name
   #employees=models.Employee.objects.all().order_by('name')
   
   #--- employee name starts with a
   #employees=models.Employee.objects.filter(name__startswith="a")
   #employees=models.Employee.objects.filter(name__istartswith="a") #not case sensitive
   
   #aggrigate functions
   min_salary = models.Employee.objects.all().aggregate(Min('salary'))
   print(min_salary)
   print(min_salary.get('salary__min'))
   minimum_salary = min_salary.get('salary__min')
   employees = models.Employee.objects.filter(salary = minimum_salary)
   print(employees)
   

   
   return render(request,'view.html',{'employees':employees})
