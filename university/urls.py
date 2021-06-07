
from django.contrib import admin
from django.urls import path, include
from djano.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
