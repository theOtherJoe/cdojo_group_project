from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# urlpatterns = [
#     path('', include('main.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)