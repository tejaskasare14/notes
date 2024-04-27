from django import template
register=template.Library()

@register.filter(name="dash_to_colon")
def dash_to_colon(value):
   new_value = value.replace("-",":")
   return new_value