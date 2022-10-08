from django.shortcuts import render
from django.http import HttpResponse
from .models import Pin

# Create your views here.
def index(request):
    return HttpResponse()
    

# def get_amount():
#     field_name = 'amount'
#     obj = Pin.objects.first()
#     field_object = Pin._meta.get_field(field_name)
#     field_value = field_object.value_from_object(obj)
#     print(field_value)

# get_amount()


