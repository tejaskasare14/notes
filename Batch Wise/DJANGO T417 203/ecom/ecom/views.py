from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from product.models import ProductTable
from django.db.models import Q

# Create your views here.
# def home(request):
#    return render(request,'base.html')



def user_login(request):
   data ={}
   if request.user.is_authenticated:
      if request.user.is_superuser:
         return redirect("/admin")
      else:
         return redirect("/")
      
      
      
   if request.method=="POST":
      uname=request.POST['username']
      upass=request.POST['password']
      
      if (uname=="" or upass==""):
         data['error_msg']="Fields cant be empty"
      elif(not User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + " user does not exist"
      else:
         user=authenticate(username=uname,password=upass)
         if user is None:
            data['error_msg']="Wrong password"
         else:
            login(request,user)
            if user.is_superuser:
               return redirect("/admin")
            else:
               return redirect("/")
   return render(request,'user/login.html',context=data)

def user_register(request):
   data ={}
   if request.user.is_authenticated:
      if request.user.is_superuser:
         return redirect("/admin")
      else:
         return redirect("/")
   if request.method=="POST":
      username=request.POST['username']
      password=request.POST['password']
      password2=request.POST['password2']
      
      if (username=="" or password=="" or password2==""):
         data['error_msg']="Fields cant be empty"
      elif(password!=password2):
         data['error_msg']="Password Does not matched"
      elif(User.objects.filter(username=username).exists()):
         data['error_msg']=username + " already exist"
      else:
         user=User.objects.create(username=username)
         user.set_password(password)
         user.save()
         return redirect("/")
   return render(request,'user/register.html',context=data)


def user_logout(request):
   logout(request)
   return redirect('/')

def admin_panel(request):
   if request.user.is_authenticated:
      if not request.user.is_superuser:
         return redirect("/")

   return render(request,'admin/admin.html')
   
# ----------------------- all logics ---------------------------------
products=ProductTable.objects.none()
def home(request):
   data={}
   global products
   global filtered_products
   products=ProductTable.objects.filter(is_available=True)
   filtered_products=products
   data['products']=products
   return render(request,'base.html',context=data)


def filter_by_category(request,category_value):
   data={}
   #select * from product where is_available=True and category=category_value
   #from django.db.models import Q
   q1 = Q(is_available=True)
   q2 = Q(category=category_value)
   global products
   global filtered_products
   filtered_products=products.filter(q1 & q2)
   data['products']=filtered_products
   return render(request,'base.html',context=data)

def sort_by_price(request,sort_value):
   data={}
   global filtered_products
   #select * from product where is_available=True order by price desc
   if(sort_value=='asc'):
      sorted_products=filtered_products.filter(is_available=True).order_by('price')
   else:
      sorted_products=filtered_products.filter(is_available=True).order_by('-price')
   data['products']=sorted_products
   return render(request,'base.html',context=data)