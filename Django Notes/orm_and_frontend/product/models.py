from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductTable(models.Model):
   CATEGORIES = ((1,'Mobile'),(2,'Clothes'),(3,'Shoes'))
   name = models.CharField(max_length=50)
   price = models.FloatField()
   details=models.CharField(max_length=150)
   category = models.IntegerField(choices=CATEGORIES)
   is_active= models.BooleanField()
   rating = models.FloatField() 
   image=models.ImageField(upload_to='image')
   
   def __str__(self) :
      return self.name + " added to table"
   
class CartTable(models.Model):
   #when you do mm without db_column attribute, you will get column name as uid_id not just uid.
   #in uid_id, id is name of PK  column of User model. if you dont want uid_id then just add
   #db_column attribute
    uid = models.ForeignKey(User,on_delete = models.CASCADE,db_column="uid")
    pid= models.ForeignKey(ProductTable,on_delete = models.CASCADE,db_column="pid") 
    quantity = models.IntegerField(default=1)
    
class OrderTable(models.Model):
   order_id=models.CharField(max_length=50)
   uid = models.ForeignKey(User,on_delete = models.CASCADE,db_column="uid")
   pid= models.ForeignKey(ProductTable,on_delete = models.CASCADE,db_column="pid") 
   quantity = models.IntegerField()
   
class CustomerDetails(models.Model):
   ADDRESS_TYPE = (('home','Home'),('office','Office'),('other','Other'))
   uid = models.ForeignKey(User,on_delete = models.CASCADE,db_column="uid")
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   phone = models.CharField(max_length=50)
   email = models.EmailField(max_length=50)
   address_type = models.CharField(max_length=10,choices=ADDRESS_TYPE)
   full_address = models.CharField(max_length=200)
   pincode = models.CharField(max_length=10)

