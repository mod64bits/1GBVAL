from django.contrib import admin
from django.urls import path, include
from apps.home import urls as home_urls

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
