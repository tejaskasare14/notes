from django.urls import path
from employee import views

urlpatterns = [
    path('add/', views.add_employee),
    path('show/', views.show_employee),
    path('delete/<empid>', views.delete_employee),
    path('update/<empid>', views.update_employee),
]