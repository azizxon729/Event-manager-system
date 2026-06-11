from django.db import models
from django.contrib.auth.models import User
from app.events.models import Event

class Registration(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Kim ro'yxatdan o'tyapti")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Qaysi tadbirga")
    registered_at = models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan vaqti")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending', verbose_name="Holati")

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"