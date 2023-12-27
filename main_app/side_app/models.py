from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.db.models import Sum


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
