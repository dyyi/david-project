import datetime
from django import template

register = template.Library()

@register.filter
def tomorrow(value):
    return value + datetime.timedelta(days=1)

@register.filter
def yesterday(value):
    return value - datetime.timedelta(days=1)    