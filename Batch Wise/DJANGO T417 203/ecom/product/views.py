from django.shortcuts import render

# Create your views here.

def add_product(request):
   return render(request,'admin/product/add_product.html')

def view_products(request):
   return render(request,'admin/product/view_product.html')
