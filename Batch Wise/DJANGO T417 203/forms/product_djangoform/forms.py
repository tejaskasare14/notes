from django import forms

class ProductForm(forms.Form):
   name = forms.CharField(max_length=50)
   PRODUCT_CATEGORY = (('cloth','CLOTH'),
                   ('mobile','MOBILE'),
                   ('shoe','SHOE'))
   category = forms.ChoiceField(choices=PRODUCT_CATEGORY)