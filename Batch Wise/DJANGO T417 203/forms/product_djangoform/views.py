from django.shortcuts import render
from product_djangoform.forms import ProductForm
from django.http import HttpResponse
from product_djangoform.models import Product

# Create your views here.
def view_product(request):
   return HttpResponse("Product added to the table")
    
def add_product(request):
   if request.method == 'POST':
      product_form=ProductForm(request.POST)
      #code to check valid data
      if(product_form.is_valid()):
         product_model=Product()
         product_model.name = product_form.cleaned_data['name']
         product_model.category = product_form.cleaned_data['category']
         product_model.save()
      return view_product(request)
   data = {}
   form=ProductForm()
   data['product_form']=form
   return render(request,'product_djangoform/add_product.html',context=data)
   
   
