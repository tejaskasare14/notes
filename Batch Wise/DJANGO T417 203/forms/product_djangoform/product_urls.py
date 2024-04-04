from django.urls import path
from product_djangoform import views
urlpatterns = [
    path('add/', views.add_product),
]