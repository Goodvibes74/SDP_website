from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Sale(models.Model):
    date        = models.DateField(auto_now_add=True)
    amount      = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True)
    created_by  = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='sales'
    )

    def __str__(self):
        return f"{self.date} – ${self.amount}"