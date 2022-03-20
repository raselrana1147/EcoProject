
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/', include('product.urls')),
    path('', include('ecommerceApp.urls')),
    path('order/', include('orderapp.urls')),
    path('user/', include('userapp.urls')),
    path('rend/', include('userapp.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



