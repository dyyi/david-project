from django.db import models
from django.utils import timezone

class PraryLog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pray_start = models.DateTimeField()
    pray_end = models.DateTimeField()
    updated_date = models.DateTimeField(default=timezone.now)