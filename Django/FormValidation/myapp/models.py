from django.db import models
from django.core import validators

# Create your models here.
class Employee(models.Model):
   name = models.CharField(max_length = 20)
   age = models.IntegerField()
   city = models.CharField(max_length = 20)

   
   
   
