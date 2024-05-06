from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from product import views
urlpatterns = [
    path('add/', views.add_product),
    path('view/', views.view_products), 
    path('delete/<productid>', views.delete_product),    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
