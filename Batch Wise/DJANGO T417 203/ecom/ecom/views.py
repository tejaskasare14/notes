from django.shortcuts import render,redirect

# Create your views here.
def home(request):
   return render(request,'base.html')


def login(request):
   data={}
   if request.method=='POST':
      # uname=request.POST['username']
      # upass=request.POST['password']
      # print(uname,upass)
      data['error_mgs'] = 'something went wrong'
      return render(request,'base.html',context=data)
   return render(request,'base.html')
