from django.shortcuts import render
from product_djangoform.forms import ProductForm

# Create your views here.
def add_product(request):
   data = {}
   form=ProductForm()
   data['product_form']=form
   return render(request,'product_djangoform/add_product.html',context=data)
   
   
