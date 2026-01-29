from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "document", "created_at")
    search_fields = ("name", "phone", "email", "document")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
