from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('api/', include('articles.urls')),
    path('api/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
    path('docs/', RedirectView.as_view(url='https://app.swaggerhub.com/apis-docs/lev4ek0/liis/1.0.0'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
