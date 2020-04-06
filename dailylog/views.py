from django.shortcuts import render
from .models import PrayLog

def praylog_list(request):
    praylogs = PrayLog.objects.all().order_by('date')
    return render(request, 'dailylog/praylog.html', {'praylogs':praylogs})