from django.db import models

# Create your models here.
class User(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   USER_DESIGNATION = (('hr','HR'),
                   ('trainer','TRAINER'),
                   ('manager','MANAGER'))
   designation = models.CharField(max_length=20,
                                  choices=USER_DESIGNATION)
   
   def __str__(self):
      return self.name + " added to the table"