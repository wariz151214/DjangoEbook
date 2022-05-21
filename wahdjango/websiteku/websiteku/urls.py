from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', include('about.urls')),
    path('buku/', include('buku.urls')),
    path('tamu/', include('tamu.urls')),
]
