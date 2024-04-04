from django.contrib import admin
from user_generalform.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
   list_display = ['id','name','designation']
admin.site.register(User,UserAdmin)
