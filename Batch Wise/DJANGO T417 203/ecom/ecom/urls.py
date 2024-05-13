"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ecom import views

urlpatterns = [
    path('admin/', views.admin_panel),
    path('', views.home),
    path('login/', views.user_login),
    path('register/', views.user_register),
    path('logout/', views.user_logout),
    path('category/<category_value>', views.filter_by_category),
    path('sort/<sort_value>', views.sort_by_price),
    path('search/', views.search_by_price_range),
    path('product/<product_id>', views.add_to_cart),
    
    path('cart/', views.show_cart),
    path('cart/delete/<cart_id>', views.delete_cart),
    path('cart/update/<flag>/<cart_id>', views.update_cart_quantity),
    
    path('order/', views.show_order),
    path('admin/product/', include('product.product_urls')),
    
    path('make-payment/', views.make_payment),
    
]
