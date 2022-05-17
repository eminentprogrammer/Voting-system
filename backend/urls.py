from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("frontend.urls")),
    path("accounts/", include("apps.account.urls")),
    path('admin/', admin.site.urls),
]
