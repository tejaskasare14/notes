from rest_framework import serializers
from employee.models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
   url = serializers.ReadOnlyField()
   eid = serializers.ReadOnlyField()
   class Meta:
      model = Employee
      fields = "__all__"