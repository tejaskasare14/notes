from django import forms
from bloodcamp.models import BloodCampRegistraion

class BloodDonorRegistraionForm(forms.ModelForm):
   
   class Meta:
      model=BloodCampRegistraion
      #fields=('name','phone')
      #exclude=['phone']
      fields='__all__'