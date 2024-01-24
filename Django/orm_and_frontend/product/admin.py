from django.contrib import admin
from product.models import ProductTable

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
   list_display = ['id','name','price','details','category','is_active','rating']
   
admin.site.register(ProductTable,ProductAdmin)
