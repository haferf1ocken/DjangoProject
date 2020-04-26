from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/testapp/', include('testapp.api.urls')),
    path('', include('testapp.urls')),
]