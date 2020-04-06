from django.shortcuts import render

def praylog_list(request):
    return render(request, 'dailylog/praylog.html', {})