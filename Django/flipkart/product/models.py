from django.db import models

# Create your models here.

class ProductTable(models.Model):
   name = models.CharField(max_length=20)
   price = models.IntegerField()
   
   def __str__(self) :
      return "product " + self.name +" added successfully"
