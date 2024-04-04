from django.db import models

# Create your models here.
class Product(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   PRODUCT_CATEGORY = (('cloth','CLOTH'),
                   ('mobile','MOBILE'),
                   ('shoe','SHOE'))
   category = models.CharField(max_length=20,
                               choices=PRODUCT_CATEGORY)
   
   def __str__(self):
      return self.name + " added to the table"