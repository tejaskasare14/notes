from django.urls import path

from product import views
urlpatterns = [
    path('add/', views.add_product),
    path('view/', views.view_products),
    
]
