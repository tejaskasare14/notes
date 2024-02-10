from django.urls import path
from bloodcamp import views

urlpatterns = [
    path('view/', views.view_donors),
    path('register/', views.register_donor),
]