from django.db import models

# Create your models here.

class Employee(models.Model):
   eid = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   salary = models.IntegerField()
   department = models.CharField(max_length=50,choices=
                                 (('IT','IT'),
                                  ('HR','HR'),
                                  ('MANAGER','MANAGER')))
   active = models.BooleanField(default=True)
   register_date = models.DateTimeField(auto_now = True)
