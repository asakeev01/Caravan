from . import settings

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.products.urls')),
    path('react/', include('apps.frontend.urls'))
]

urlpatterns += static(settings.MEDIA_ROOT, document_root = settings.MEDIA_ROOT)