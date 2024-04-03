from django.db import models

# Create your models here.
class Product(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   description = models.CharField(max_length=150)
   price = models.IntegerField()
   
   def __str__(self) :
      return self.name + " added to the table"
   
