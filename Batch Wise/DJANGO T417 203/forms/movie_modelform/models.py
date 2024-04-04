from django.db import models

# Create your models here.
class Movie(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=50)
   MOVIE_GENERE = (('comedy','COMEDY'),
                   ('action','ACTION'),
                   ('crime','CRIME'))
   genere = models.CharField(max_length=20,
                             choices=MOVIE_GENERE)
   
   def __str__(self):
      return self.name + " added to the table"
