from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Sistema de Orçamentos"
admin.site.site_title = "Administração"
admin.site.index_title = "Painel do Sistema"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
