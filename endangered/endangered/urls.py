from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('species/', include('species.urls')),
    path('admin/', admin.site.urls),
]
