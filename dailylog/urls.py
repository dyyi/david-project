from django.urls import path
from . import views

urlpatterns = [
    path('', views.praylog_list, name='praylog_list'),
    path('praylog/<str:target_date>/', views.praylog_detail, name='praylog_detail'),
]