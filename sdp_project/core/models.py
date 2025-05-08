from django.db import models
from django.conf import settings
from django.contrib.auth.models import User ,AbstractUser 

class CustomUser(AbstractUser):
    # Add any additional fields you want to include in your custom user model
    email = models.EmailField(unique=True, blank=False, null=False)

class Sale(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('closed', 'Closed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return self.title


