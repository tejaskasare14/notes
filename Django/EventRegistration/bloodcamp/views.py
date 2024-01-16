from django.shortcuts import render
from bloodcamp import models
from bloodcamp import forms

# Create your views here.
def view_donors(request):
   data=models.BloodCampRegistraion.objects.all()
   all_donors = {'donors':data}
   return render(request,'bloodcamp/view_donors.html',context=all_donors)

def register_donor(request):
   registration_form = forms.BloodDonorRegistraionForm()
   form = {'form':registration_form}
   if (request.method=='POST'):
      form_data = forms.BloodDonorRegistraionForm(request.POST)
      if (form_data.is_valid()):
         form_data.save(commit=True)
         return view_donors(request)
   return render(request,'bloodcamp/register_donor.html',context=form)
