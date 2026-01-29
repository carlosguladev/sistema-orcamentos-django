from django.contrib import admin
from .models import CatalogItem

@admin.register(CatalogItem)
class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ("name", "unit", "unit_price", "is_service", "active", "created_at")
    search_fields = ("name",)
    list_filter = ("is_service", "active", "unit")
    ordering = ("name",)
    list_editable = ("unit_price", "active")  # edita direto na lista
