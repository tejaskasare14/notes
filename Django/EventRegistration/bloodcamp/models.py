from django.db import models

# Create your models here.

class BloodCampRegistraion(models.Model):
   name = models.CharField(max_length=20)
   phone = models.CharField(max_length=20)
   city = models.CharField(max_length=20)
   
   def __str__(self):
      return "Hi " + self.name + " registration success!!!"
