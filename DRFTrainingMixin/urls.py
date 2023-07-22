from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('Mixins1.urls')),
    path('api/v1/', include('Mixins2.urls')),
    path('api/v1/', include('Mixins3.urls')),
    path('api/v1/', include('Mixins4.urls')),
]
