from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register_user(request):
   data={}
   # checking user is alredy authenticated then redirect to home page
   if request.user.is_authenticated:
      return redirect('/myapp/home')
   
   if request.method=='POST':
      uname=request.POST['username']
      upass=request.POST['password']
      uconf_pass=request.POST['password2']
      if(uname=='' or upass=='' or uconf_pass==''):
         data['error_msg']="fields cant be empty"
         return render(request,'myapp/register.html',context=data)
      elif(upass!=uconf_pass):
         data['error_msg']="passwords does not matched"
         return render(request,'myapp/register.html',context=data)
      elif(User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + " alredy exist"
         return render(request,'myapp/register.html',context=data)
      else:  
         new_user=User.objects.create(username=uname)
         new_user.set_password(upass)
         new_user.save()
         return HttpResponse("Registration done")
   return render(request,'myapp/register.html')


def login_user(request):
   data={}
   # checking user is alredy authenticated then redirect to home page
   if request.user.is_authenticated:
      return redirect('/myapp/home')
    
   if request.method=='POST':
      uname=request.POST['username']
      upass=request.POST['password']
      if(uname=='' or upass==''):
         data['error_msg']="fields cant be empty"
         return render(request,'myapp/login.html',context=data)
      elif(not User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + " does not exist"
         return render(request,'myapp/login.html',context=data)
      else:  
         #If the given credentials are valid, then return a User object otherwise None
         # from django.contrib.auth import authenticate 
         user=authenticate(username=uname,password=upass)
         print(user)
         if user is None:
            data['error_msg']="Invalid passowrd"
            return render(request,'myapp/login.html',context=data)
         else:
            login(request,user)
            return redirect('/myapp/home')
   return render(request,'myapp/login.html')


def home(request):
   data={}
   data["user_name"] = "User"
   if request.user.is_authenticated:
      user_id=request.user.id
      user_based_on_id=User.objects.get(id=user_id)
      print(user_based_on_id.username)
      username = user_based_on_id.username
      data["user_name"] = username
   return render(request,'myapp/home.html',context=data)

def user_logout(request):
   logout(request)
   return redirect('/myapp/home')
