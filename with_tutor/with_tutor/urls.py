from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', include('about.urls', namespace='about')),
    path('vocabulary/', include('vocabulary.urls', namespace='vocabulary')),
    path('grammar/', include('grammar.urls', namespace='grammar')),
    path('reading/', include('reading.urls', namespace='reading')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)