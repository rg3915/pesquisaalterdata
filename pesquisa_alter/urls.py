from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pesquisa_alter.core.urls')),
    path('admin/', admin.site.urls),
]
