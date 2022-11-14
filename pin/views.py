from django.shortcuts import render, redirect
import random
import hashlib
import base64
import pyotp
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .models import Pin
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def generate_pin_form(request):
    return render(request, 'change_form.html')

@require_http_methods(["POST"])
def generate_pin(request):
        data = request.POST
        amount = data.get('amount', 5)
        value = int(data.get('value', 100))
        if amount:
            pinIds = []
            for i in range(int(amount)):
                pin = random.randint(100000, 999999)
                hash = hashlib.md5(str(pin).encode('utf-8')).hexdigest()
                hash = base64.b32encode(bytearray(settings.SECRET_KEY + hash, 'ascii')).decode('utf-8')
                new_pin = Pin(pin=pin, secret=hash, value=value)
                new_pin.save()
                pinIds.append(new_pin.id)
            return redirect('/print-pins/?pinIds=' + ','.join(map(str, pinIds)))
        else:
            return HttpResponse('Please enter a valid amount')

@require_http_methods(["GET"])
def print_pins(request):
    pinIds = request.GET.get('pinIds')
    pins = Pin.objects.filter(id__in=pinIds.split(','), status='valid')
    phone = "07040199716"
    return render(request, 'print_pins.html', {'pins': pins, 'phone': phone })
