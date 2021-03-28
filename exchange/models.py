from django.db import models

class Exchange(models.Model):

    Exchange_rate = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    margin = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-created_at']
