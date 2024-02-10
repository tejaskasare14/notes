from django.contrib import admin
from movie.models import Movies

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
   list_display = ["id","movie_name", "release_date"]

admin.site.register(Movies,MovieAdmin)
