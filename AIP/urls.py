from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home.urls')),  # this address is for home app
                  path('services', include('services.urls')) , # this address is for services app
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
