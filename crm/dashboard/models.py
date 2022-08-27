from urllib import request
from django.db import models

# Create your models here.
class Metrics(models.Model):
    request = models.JSONField(blank=True)
    total_count_users = models.IntegerField(blank=True)
    count_users = models.IntegerField(blank=True)
    total_count_session = models.IntegerField(blank=True)
    consersion_purchases = models.FloatField(blank=True)
    consersion_products = models.FloatField(blank=True)
    roi = models.FloatField(blank=True)
    abandoned_carts = models.FloatField(blank=True)
    revenue_per_transaction = models.FloatField(blank=True)