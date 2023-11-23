#chkimsv20/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventory/", include("inventory.urls")),
    path("", auth_views.LoginView.as_view(template_name = "inventory_systems/login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name = "inventory_systems/logout.html"), name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
