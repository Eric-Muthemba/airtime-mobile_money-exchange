from django.db import models
from exchange.models import Exchange

class Transactions(models.Model):

    TYPE_OF_TRANSACTION = [
        ('A2M', 'A2M'),
        ('M2A', 'M2A'),
    ]

    category = models.CharField(choices=TYPE_OF_TRANSACTION, max_length=30)
    credit_amount = models.DecimalField(max_digits=10, decimal_places=0, max_length=255)
    cash_amount = models.DecimalField(max_digits=10, decimal_places=0, max_length=255)
    from_phoneNumber = models.DecimalField(max_digits=10,decimal_places=0, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)