from django.db import models

# Create your models here.

class ProductTable(models.Model):
   id=models.AutoField(primary_key=True)
   name=models.CharField(max_length=100)
   price=models.IntegerField()
   description=models.CharField(max_length=100)
   quantity=models.IntegerField()
   category=models.CharField(max_length=100)
   image=models.ImageField(upload_to='image')
   is_available=models.BooleanField()
   
