from django.db import models
from django.contrib.auth.models import User


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
   
class CartTable(models.Model):
   #uid_id
   uid = models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
   pid = models.ForeignKey(ProductTable,on_delete=models.CASCADE,db_column='pid')
   quantity=models.IntegerField()
