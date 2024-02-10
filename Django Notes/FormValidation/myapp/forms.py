from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


def name_start_with_a(name):
   if(name[0].lower() != 'a'):
      raise ValidationError("Name Must be start with a OR A")
      
   
class EmployeeForm(forms.Form):
   name = forms.CharField(max_length = 20,validators=[validators.MaxLengthValidator(20),validators.MinLengthValidator(3),name_start_with_a])
   age = forms.IntegerField(validators=[validators.MinValueValidator(18)])
   city = forms.CharField(max_length = 20)
  
   def clean_city(self) :
      city=self.cleaned_data['city']
      if(len(city)<2):
         raise ValidationError("Min characters for city name are 2")
      return city