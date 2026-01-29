from django.db import models

class CatalogItem(models.Model):
    UNIT_CHOICES = [
        ("m", "Metro"),
        ("un", "Unidade"),
        ("hr", "Hora"),
    ]

    name = models.CharField("Nome", max_length=120)
    unit = models.CharField("Unidade", max_length=10, choices=UNIT_CHOICES, default="un")
    unit_price = models.DecimalField("Preço unitário", max_digits=10, decimal_places=2)
    is_service = models.BooleanField("É serviço?", default=True)

    active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"
