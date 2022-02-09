from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('articles.urls')),
    path('api/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]
