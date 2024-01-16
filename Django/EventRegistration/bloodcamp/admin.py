from django.contrib import admin
from bloodcamp.models import *

# Register your models here.
class BloodCampRegistraionAdmin(admin.ModelAdmin):
   list_display = ['id','name','phone','city']
   
admin.site.register(BloodCampRegistraion,BloodCampRegistraionAdmin)
   

