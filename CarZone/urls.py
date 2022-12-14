from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('cars.urls')),
    path('', include('accounts.urls')),
    path('', include('contacts.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
