from django.urls import path,include
from rest_framework import routers
from employee.views import EmployeeViewSet
from employee.models import Employee

router=routers.DefaultRouter()
router.register('employees',EmployeeViewSet,basename='Employee')
urlpatterns = [
    path('',include(router.urls)),
]
