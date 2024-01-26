from django.shortcuts import render
from django.http import HttpResponse
from product.models import ProductTable
from django.db.models import Q

# Create your views here.
def index(request):
   data={}
   #ProductTable.objects.all() this will fetch non active product also. so it is better to use filter
   fetched_products=ProductTable.objects.filter(is_active=True)
   data['products']=fetched_products
   return render(request,'product/index.html',context=data)

def filter_by_category(request,category_value):
   #select * from product where is_active=True and category=category_value;
   #ProductTable.objects.filter(is_active=True , category=category_value)
   #from django.db.models import Q
   data={}
   q1 = Q(is_active=True)
   q2 = Q(category=category_value)
   filterd_products=ProductTable.objects.filter(q1 & q2)
   data['products']=filterd_products
   return render(request,'product/index.html',context=data)

def sort_by_price(request,sort_value):
   #select * from product order by salary desc;
   data={}
   if sort_value=='asc':
      price = 'price'
   else:
      price = '-price'
   sorted_products=ProductTable.objects.filter(is_active=True).order_by(price)
   data['products']=sorted_products
   return render(request,'product/index.html',context=data)

def filter_by_rating(request,rating_value):
   #select * from product where is_active=True and category=category_value;
   #ProductTable.objects.filter(is_active=True , category=category_value)
   #from django.db.models import Q
   data={}
   q1 = Q(is_active=True)
   q2 = Q(rating__gt=rating_value)
   filterd_products=ProductTable.objects.filter(q1 & q2)
   data['products']=filterd_products
   return render(request,'product/index.html',context=data)


def filter_by_price_range(request):
   data={}
   min = request.GET['min']
   max = request.GET['max']
   q1 = Q(price__gte=min)
   q2 = Q(price__lte=max)
   q3 = Q(is_active=True)
   filterd_products=ProductTable.objects.filter(q1 & q2 & q3)
   data['products']=filterd_products
   return render(request,'product/index.html',context=data)