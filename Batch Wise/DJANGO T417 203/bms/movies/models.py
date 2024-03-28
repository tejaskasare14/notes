from django.db import models

# Create your models here.
class Movie(models.Model):
   movie_id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   rating = models.FloatField()
   genere = models.CharField(max_length=50)
