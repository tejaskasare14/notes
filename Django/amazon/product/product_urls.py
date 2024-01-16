from django.urls import path
from product import views

urlpatterns = [
    path('view/', views.view_product),
    path('add/', views.add_product),
]

