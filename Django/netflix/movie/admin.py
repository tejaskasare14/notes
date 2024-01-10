from django.contrib import admin
from movie.models import MovieTable

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
   list_display = ['id','name','release_date','in_theater','rating','language']


admin.site.register(MovieTable,MovieAdmin)