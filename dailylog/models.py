from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date

class PrayLog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    start = models.TimeField(null=True)
    end = models.TimeField(null=True)
    start_goal = models.TimeField(blank=True, null=True)
    end_goal = models.TimeField(blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author.username + "'s " + str(self.date)