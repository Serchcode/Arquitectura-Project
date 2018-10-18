from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from main import urls as HomeUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(("main.urls","main"),namespace="main")),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
