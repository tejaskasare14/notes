from django.db import models

# Create your models here.

class Movies(models.Model):
   #django automatically provide id to each record by default. so no need to create id field
   movie_name = models.CharField(max_length=20)
   release_date  = models.DateField()
   
