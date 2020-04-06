from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date

class PrayLog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    pray_start = models.DateTimeField()
    pray_end = models.DateTimeField()
    updated_date = models.DateTimeField(default=timezone.now)