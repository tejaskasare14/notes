from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import ProductTable,CartTable
from django.db.models import Q

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
   data={}
   #ProductTable.objects.all() this will fetch non active product also. so it is better to use filter
   fetched_products=ProductTable.objects.filter(is_active=True)
   data['products']=fetched_products
   #getting count of cart item for specific user
   user_id=request.user.id
   id_specific_cartitems=CartTable.objects.filter(uid=user_id)
   count=id_specific_cartitems.count()
   data['cart_count']=count
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

def product_detail(request,pid):
   product=ProductTable.objects.get(id=pid)
   return render(request,'product/product_detail.html',{'product':product})

def register_user(request):
   data={}
   if request.method=="POST":
      uname=request.POST['username']
      upass=request.POST['password']
      uconf_pass=request.POST['password2']
      #implementing validation
      if (uname=='' or upass =='' or uconf_pass ==''):
         data['error_msg']='Fileds cant be empty'
         return render(request,'user/register.html',context=data)
      elif(upass!=uconf_pass):
         data['error_msg']='Password and confirm password does not matched'
         return render(request,'user/register.html',context=data)
      elif(User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + ' alredy exist'
         return render(request,'user/register.html',context=data)
      else:
         user=User.objects.create(username=uname)
         #here username and password aee column names present inside auth_user table
         user.set_password(upass) #encrypting passowrd
         user.save() #saving data into table
         customer=CustomerDetails.objects.create(uid=user)
         customer.save()
         # return HttpResponse("Registraion done") 
         return redirect('/user/login')
   return render(request,'user/register.html')

def login_user(request):
   data={}
   if request.method=="POST":
      uname=request.POST['username']
      upass=request.POST['password']
      #implementing validation
      if (uname=='' or upass ==''):
         data['error_msg']='Fileds cant be empty'
         return render(request,'user/login.html',context=data)
      elif(not User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + ' user is not registered'
         return render(request,'user/login.html',context=data)
      else:
         #from django.contrib.auth import authenticate
         user=authenticate(username=uname,password=upass)
         print(user)
         if user is not None:
            login(request,user)
            return redirect('/product/index')
         else:
            data['error_msg']='Wrong Password'
            return render(request,'user/login.html',context=data)   
   return render(request,'user/login.html')

def user_logout(request):
   logout(request)
   return redirect('/product/index')

def add_to_cart(request,pid):
   if request.user.is_authenticated:
      uid = request.user.id
      print("user id = " ,uid)
      print("product id = ", pid)
      #we cant pass only id in cart table, it is expecting object of User and Product
      #therefore below line will gives error
      #cart=CartTable.objects.create(pid=pid,uid=uid)
      user=User.objects.get(id=uid)
      product=ProductTable.objects.get(id=pid)
      
      q1 = Q(uid=uid)
      q2 = Q(pid=pid)
      available_products=CartTable.objects.filter(q1 & q2)
      print()
      if(available_products.count()>0):
         messages.error(request, 'Product is alredy in the cart.')
         return redirect('/product/index') 
      else:
         cart=CartTable.objects.create(pid=product,uid=user)
         cart.save()
         messages.success(request,"Product is added to the cart.")
         return redirect('/product/index')  
   else:
      return redirect("/user/login")
   
def view_cart(request):
   data ={}
   user_id=request.user.id
   user=User.objects.get(id = user_id)
   id_specific_cartitems=CartTable.objects.filter(uid=user_id)
   data['products']=id_specific_cartitems
   data['user']=user
   #couting total items in cart
   count=id_specific_cartitems.count()
   #data['cart_count']=count
   #couting total price of cart
   total_price = 0
   total_quantity=0
   for item in id_specific_cartitems:
      #print(item.pid.price)
      #total_price+=item.pid.price
      total_price=(total_price+item.pid.price)*(item.quantity)
      total_quantity+=item.quantity
   data['total_price']=total_price
   data['cart_count']=total_quantity
   return render(request,'product/cart.html',context=data)

def remove_item(request,cartid):
   cart=CartTable.objects.get(id=cartid)
   cart.delete()
   return  redirect('/product/view_cart')

def update_quantity(request,flag,cartid):
   #print(type(flag))
   cart=CartTable.objects.filter(id=cartid)
   actual_quantity = cart[0].quantity
   if(flag=="1"):
      cart.update(quantity = actual_quantity+1)
      pass
   else:
      if(actual_quantity>1):
         cart.update(quantity = actual_quantity-1)
      pass
   return redirect('/product/view_cart')

# import calendar
# import time
# from product.models import OrderTable
# def place_order(request):
#    data={}
#    current_GMT = time.gmtime()
#    time_stamp = calendar.timegm(current_GMT)
#    user_id = request.user.id
#    oid=str(user_id)+"-"+str(time_stamp)
#    #in above line we have created custome order id by combining user id and current time stamp
#    cart=CartTable.objects.filter(uid=user_id)
#    for data in cart:
#       # print(data.id, data.pid, data.uid, data.quantity, sep="--")
#       order=OrderTable.objects.create(order_id=oid,quantity=data.quantity,pid=data.pid,uid=data.uid)
#       order.save()
#       cart.delete()
#    order=OrderTable.objects.filter(uid=user_id)
#    total_price = 0
#    total_quantity=0
#    for item in order:
#       total_price=(total_price+item.pid.price)*(item.quantity)
#       total_quantity+=item.quantity
#    data['products']=order   
#    data['total_price']=total_price
#    data['cart_count']=total_quantity
#    return render(request,'product/order.html',context=data)


def place_order(request):
   data ={}
   user_id=request.user.id
   user=User.objects.get(id = user_id)
   id_specific_cartitems=CartTable.objects.filter(uid=user_id)
   customer = CustomerDetails.objects.get(uid = user_id)
   data['customer']=customer
   data['products']=id_specific_cartitems
   data['user']=user
   total_price = 0
   total_quantity=0
   for item in id_specific_cartitems:
      total_price=(total_price+item.pid.price)*(item.quantity)
      total_quantity+=item.quantity
   data['total_price']=total_price
   data['cart_count']=total_quantity
   return render(request,'product/order.html',context=data)

from product.models import CustomerDetails
def edit_profile(request):
   data={}
   user_id=request.user.id
   customer_querySet=CustomerDetails.objects.filter(uid=user_id)
   customer = customer_querySet[0]
   data['customer']=customer
   if request.method=="POST":
      first_name=request.POST['first_name']
      last_name=request.POST['last_name']
      phone=request.POST['phone']
      email=request.POST['email']
      address_type=request.POST['address_type']
      full_address=request.POST['full_address']
      pincode=request.POST['pincode']
      print(first_name,last_name,phone,email,address_type,full_address,pincode)
      customer_querySet.update(first_name=first_name,last_name=last_name,phone=phone,email=email,address_type=address_type,full_address=full_address,pincode=pincode)
      return redirect('/product/index')
   return render(request,'user/edit_profile.html',context=data)

import razorpay   
def make_payment(request):
   #getting total amount
   user_id=request.user.id
   id_specific_cartitems=CartTable.objects.filter(uid=user_id)
   total_price = 0
   for item in id_specific_cartitems:
      total_price=(total_price+item.pid.price)*(item.quantity) 
      
   client = razorpay.Client(auth=("rzp_test_ls3ufyYec3WWtv", "Cm3iRE0s8JpvOE5hTg9dS8tP"))
   data = { "amount": total_price*100, "currency": "INR", "receipt": "order_rcptid_11" }
   payment = client.order.create(data=data)
   print(payment)
   #return HttpResponse("Payment Done")
   return render(request,'product/pay.html',context=data)