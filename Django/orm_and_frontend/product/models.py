from django.db import models

# Create your models here.
class ProductTable(models.Model):
   CATEGORIES = ((1,'Mobile'),(2,'Clothes'),(3,'Shoes'))
   name = models.CharField(max_length=50)
   price = models.FloatField()
   details=models.CharField(max_length=150)
   category = models.IntegerField(choices=CATEGORIES)
   is_active= models.BooleanField()
   rating = models.FloatField() 
   
   def __str__(self) :
      return self.name + " added to table"