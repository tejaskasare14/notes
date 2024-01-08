from django.contrib import admin
from product.models import ProductTable

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
   list_display= ["id","name", "price"]

admin.site.register(ProductTable,ProductAdmin)
