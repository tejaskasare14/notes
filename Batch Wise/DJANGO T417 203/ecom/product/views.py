from django.shortcuts import render,redirect
from product.models import ProductTable

# Create your views here.

def add_product(request):
   if request.method=='POST':
      name=request.POST.get('name')
      price=request.POST.get('price')
      description=request.POST.get('description')
      quantity=request.POST.get('quantity')
      category=request.POST.get('category')
      image = request.FILES.get('image')
      is_available=(request.POST.get('is_available',False)) and ('is_available' in request.POST)
      
      product=ProductTable.objects.create(name=name,price=price,description=description,quantity=quantity,category=category,image=image,is_available=is_available)
      
      product.save()
      
      return redirect("/admin/product/view/")
   return render(request,'admin/product/add_product.html')

def view_products(request):
   return render(request,'admin/product/view_product.html')
