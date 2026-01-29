from django.contrib import admin
from .models import Quote, QuoteLine

class QuoteLineInline(admin.TabularInline):
    model = QuoteLine
    extra = 1
    autocomplete_fields = ("item",)  # campo item vira busca
    fields = ("item", "description", "quantity", "unit_price", "line_total")
    readonly_fields = ("line_total",)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "created_at", "subtotal", "total")
    list_filter = ("status", "created_at")
    search_fields = ("customer__name", "id")
    ordering = ("-created_at",)
    inlines = [QuoteLineInline]

    # travar campos que o Django preenche sozinho
    readonly_fields = ("created_by", "public_token", "created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
