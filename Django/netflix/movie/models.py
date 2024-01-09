from django.db import models

# Create your models here.

class MovieTable(models.Model):
   name=models.CharField(max_length=15)
   release_date=models.DateField()
   INTHEATERS_CHOICES = (
   ('yes', 'Yes'),
   ('no', 'No'))
   in_theater = models.CharField(choices=INTHEATERS_CHOICES,max_length=5)
   rating = models.FloatField()
   LANGUAGE_CHOICES = (
   ('hindi', 'Hindi'),
   ('marathi', 'Marathi'),
   ('english', 'English'))
   language = models.CharField(choices=LANGUAGE_CHOICES,max_length=15)
   
