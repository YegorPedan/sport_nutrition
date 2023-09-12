from django.urls import path

from .views import Index, ShowProduct

app_name = 'shop'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('product/<int:pk>/', ShowProduct.as_view(), name='product-detail'),
]
