from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from places import views
from places.views import show_place


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start_page),
    path('organizer/<int:id>/', show_place, name='organizer'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
