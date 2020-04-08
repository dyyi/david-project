from django.shortcuts import render, get_object_or_404
from .models import PrayLog
from datetime import datetime, date


def praylog_list(request):
    praylogs = PrayLog.objects.all().filter(author=request.user).order_by('date')
    return render(request, 'dailylog/praylog.html', {'praylogs':praylogs, 'today': date.today()})

def praylog_detail(request, target_date):
    try:
        praylog = PrayLog.objects.get(author=request.user, date=target_date)
    except:
        praylog = PrayLog()
        praylog.author = request.user
        praylog.date = datetime.strptime(target_date, "%Y-%m-%d").date
    return render(request, 'dailylog/praylog_detail.html', {'praylog': praylog, 'today': date.today()})

