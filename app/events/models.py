from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Tadbir nomi")
    description = models.TextField(verbose_name="Tadbir haqida")
    date = models.DateTimeField(verbose_name="Tadbir sanasi va vaqti")
    location = models.CharField(max_length=255, verbose_name="Manzil")
    capacity = models.PositiveIntegerField(verbose_name="Maksimal ishtirokchilar soni")
    image = models.ImageField(upload_to='events/', verbose_name="Tadbir rasmi", null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Tadbir holati")

    def __str__(self):
        return self.title