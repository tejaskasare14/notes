from django.shortcuts import render,redirect
from django.http import HttpResponse
#importing User model to store user data
from django.contrib.auth.models import User

#importing autheticate function to login user
from django.contrib.auth import authenticate,login,logout
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
            login(request,user)
            return redirect('/myapp/home')
         else:
            data['error_msg']='Wrong Password'
            return render(request,'myapp/login.html',context=data)   
   return render(request,'myapp/login.html')

def home(request):
   data = {}
   #checking whether user is authenticated user
   user_authenticated=request.user.is_authenticated
   print(user_authenticated)
   #if authenticated, then show home else go to login page
   if(user_authenticated):
      user_id = request.user.id 
      user=User.objects.get(id=user_id)
      # print(user_id)
      data['user_data'] = user.username
      return render(request,'myapp/home.html',context=data)
   else:
      #control came here because user is not logged in
      # so you can redirect to login page
      data['user_data'] = "User"
      return render(request,'myapp/home.html',context=data)
   
def user_logout(request):
   logout(request)
   return render(request,'myapp/home.html',{'user_data':"User"})
         
