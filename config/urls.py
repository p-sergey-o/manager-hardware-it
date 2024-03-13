from django.contrib import admin
from django.urls import include
from django.urls import path

from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/', include('server.urls')),
]

urlpatterns += doc_urls
