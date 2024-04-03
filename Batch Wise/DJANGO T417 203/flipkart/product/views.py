from django.shortcuts import render
from product.models import Product
# Create your views here.
def show_product(request):
   data ={}
   all_products = Product.objects.all()
   data['products'] = all_products
   data['name']  = "Raj"
   return render(request,'product/index.html',context=data)
