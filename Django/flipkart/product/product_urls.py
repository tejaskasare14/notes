from django.urls import path
from product import views

urlpatterns = [
    path('view/',views.view_products),
]
