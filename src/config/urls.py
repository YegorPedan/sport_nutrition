from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('admin', admin.site.urls),
    path('', RedirectView.as_view(url='shop/')),
    path('shop/', include('apps.shop.urls', namespace='shop/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
