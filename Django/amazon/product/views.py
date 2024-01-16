from django.shortcuts import render,redirect
from product.models import Product
from product.forms import ProductForm

# Create your views here.
def view_product(request):
   all_products=Product.objects.all()
   data = {'products':all_products}
   return render(request,'product/view_product.html',context=data)

def add_product(request):
   if(request.method=='GET'):
      product_form = ProductForm()
      form = {'form':product_form}
      return render(request,'product/add_product.html',context=form)
   else:
      form_data = ProductForm(request.POST)
      if (form_data.is_valid()):
         form_data.save(commit=True)
         return redirect('/product/view')