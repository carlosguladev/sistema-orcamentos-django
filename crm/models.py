from django.db import models

class Customer(models.Model):
    name = models.CharField("Nome", max_length=120)
    phone = models.CharField("Telefone", max_length=30, blank=True)
    email = models.EmailField("Email", blank=True)
    document = models.CharField("CPF/CNPJ", max_length=30, blank=True)
    address = models.CharField("Endereço", max_length=255, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
