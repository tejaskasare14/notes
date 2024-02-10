from django.shortcuts import render
from product.models import ProductTable

# Create your views here.
def view_products(request):
   result = ProductTable.objects.all()
   print(result)
   data = {'product_list':result}
   return render(request,'product/view_products.html',context=data)