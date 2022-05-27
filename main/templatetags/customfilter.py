from django import template

from main.forms import EVENT_REG
from main.models import event_reg
# from .models import *
register = template.Library()

@register.filter
def lower(value):
    return value.lower()

# @register.filter
# def count(ename):
#     obj = event_reg.objects.filter(event__exact = ename)
#     print(obj)
#     x = count(obj)
#     return x