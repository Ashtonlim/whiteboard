from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('frontend.urls')),
    path('', include('vidboard.urls')),
    path('admin/', admin.site.urls),
]


# This is unecessary but adding for readability. urls are only added when in debug mode even w/o if cond
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)