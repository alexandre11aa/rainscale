from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('user.urls')),
    # path('', include('location.urls')),
    # path('', include('experiment.urls')),
    path('', include('model.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)