from django.urls import path
from product import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index),
    path('filter/<category_value>', views.filter_by_category),
    path('sort/<sort_value>', views.sort_by_price),
    path('rating/<rating_value>', views.filter_by_rating),
    path('price', views.filter_by_price_range),
    path('product_detail/<pid>', views.product_detail),
    path('add_to_cart/<pid>', views.add_to_cart),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)