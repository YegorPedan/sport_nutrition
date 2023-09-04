from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('shop/')),
    path('shop/', include('apps.shop.urls', namespace='shop/')),
    path('admin/', admin.site.urls),
]
