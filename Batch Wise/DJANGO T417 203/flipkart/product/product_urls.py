from django.urls import path
from product import views
urlpatterns = [
    path('get/', views.show_product),
]