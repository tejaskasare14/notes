from django.contrib import admin
from movie_modelform.models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
   list_display = ['id','name','genere']
admin.site.register(Movie,MovieAdmin)
