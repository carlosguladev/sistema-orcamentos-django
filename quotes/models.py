import uuid
from decimal import Decimal

from django.conf import settings
from django.db import models


class Quote(models.Model):
    STATUS_CHOICES = [
        ("draft", "Rascunho"),
        ("sent", "Enviado"),
        ("approved", "Aprovado"),
        ("canceled", "Cancelado"),
    ]

    DISCOUNT_TYPE_CHOICES = [
        ("none", "Sem desconto"),
        ("fixed", "Desconto em R$"),
        ("percent", "Desconto em %"),
    ]

    customer = models.ForeignKey(
        "crm.Customer",
        on_delete=models.PROTECT,
        related_name="quotes"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="quotes"
    )

    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default="draft")

    discount_type = models.CharField(
        "Tipo de desconto",
        max_length=20,
        choices=DISCOUNT_TYPE_CHOICES,
        default="none"
    )
    discount_value = models.DecimalField(
        "Valor do desconto",
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00")
    )

    notes = models.TextField("Observações", blank=True)

    public_token = models.UUIDField(
        "Token público",
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    def __str__(self):
        return f"Orçamento #{self.id} - {self.customer}"

    @property
    def subtotal(self):
        total = Decimal("0.00")
        for line in self.lines.all():
            total += (line.quantity * line.unit_price)
        return total

    @property
    def discount_amount(self):
        subtotal = self.subtotal

        if self.discount_type == "fixed":
            return min(self.discount_value, subtotal)

        if self.discount_type == "percent":
            pct = max(Decimal("0.00"), min(self.discount_value, Decimal("100.00")))
            return (subtotal * pct / Decimal("100.00")).quantize(Decimal("0.01"))

        return Decimal("0.00")

    @property
    def total(self):
        value = self.subtotal - self.discount_amount
        return max(Decimal("0.00"), value)

    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"


class QuoteLine(models.Model):
    quote = models.ForeignKey(
        Quote,
        on_delete=models.CASCADE,
        related_name="lines"
    )
    item = models.ForeignKey(
        "catalog.CatalogItem",
        on_delete=models.PROTECT
    )

    description = models.CharField("Descrição (opcional)", max_length=200, blank=True)

    quantity = models.DecimalField(
        "Quantidade",
        max_digits=10,
        decimal_places=2,
        default=Decimal("1.00")
    )
    unit_price = models.DecimalField(
    "Preço unitário",
    max_digits=10,
    decimal_places=2,
    default=Decimal("0.00")
)
    sort_order = models.PositiveIntegerField("Ordem", default=0)

    def __str__(self):
        return f"{self.item} x {self.quantity}"

    @property
    def line_total(self):
        return (self.quantity * self.unit_price).quantize(Decimal("0.01"))

    def save(self, *args, **kwargs):
        # se não tiver preço, copia do item
        if self.unit_price is None:
            self.unit_price = self.item.unit_price

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Item do orçamento"
        verbose_name_plural = "Itens do orçamento"
