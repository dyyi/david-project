from django.urls import path
from . import views

urlpatterns = [
    path('', views.praylog_list, name='praylog_list'),
]