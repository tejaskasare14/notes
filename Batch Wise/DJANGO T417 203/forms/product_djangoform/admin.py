from django.contrib import admin
from product_djangoform.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
   list_display = ['id','name','category']
admin.site.register(Product,ProductAdmin)

