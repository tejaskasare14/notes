from django.shortcuts import render,redirect
from django.http import HttpResponse
#importing User model to store user data
from django.contrib.auth.models import User

#importing autheticate function to login user
from django.contrib.auth import authenticate
# Create your views here.
def register_user(request):
   data={}
   if request.method=="POST":
      uname=request.POST['username']
      upass=request.POST['password']
      uconf_pass=request.POST['password2']
      #implementing validation
      if (uname=='' or upass =='' or uconf_pass ==''):
         data['error_msg']='Fileds cant be empty'
         return render(request,'myapp/register.html',context=data)
      elif(upass!=uconf_pass):
         data['error_msg']='Password and confirm password does not matched'
         return render(request,'myapp/register.html',context=data)
      elif(User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + ' alredy exist'
         return render(request,'myapp/register.html',context=data)
      else:
         user=User.objects.create(username=uname)
         #here username and password aee column names present inside auth_user table
         user.set_password(upass) #encrypting passowrd
         user.save() #saving data into table
         return HttpResponse("Registraion done")  
   return render(request,'myapp/register.html')

def login_user(request):
   data={}
   if request.method=="POST":
      uname=request.POST['username']
      upass=request.POST['password']
      #implementing validation
      if (uname=='' or upass ==''):
         data['error_msg']='Fileds cant be empty'
         return render(request,'myapp/login.html',context=data)
      elif(not User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + ' user is not registered'
         return render(request,'myapp/login.html',context=data)
      else:
         #from django.contrib.auth import authenticate
         user=authenticate(username=uname,password=upass)
         print(user)
         if user is not None:
            return redirect('/myapp/home')
         else:
            data['error_msg']='Wrong Password'
            return render(request,'myapp/login.html',context=data)   
   return render(request,'myapp/login.html')

def home(request):
   return render(request,'myapp/home.html')
