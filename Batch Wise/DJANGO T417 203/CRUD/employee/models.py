from django.db import models

# Create your models here.
class EmployeeTable(models.Model):
   id=models.AutoField(primary_key=True)
   name=models.CharField(max_length=50)
   salary=models.FloatField()
   DESIGNATION = (('hr','HR'),
                  ('manager','MANAGER'),
                  ('trainer','TRAINER'))
   designation=models.CharField(choices=DESIGNATION,max_length=30)
