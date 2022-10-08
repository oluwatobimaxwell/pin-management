from django.shortcuts import render, redirect
import random
import hashlib
import base64
import pyotp
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .models import Pin


def generate_pin(request):
        data = request.GET
        amount = data.get('amount')
        if amount:
            for i in range(int(amount)):
                pin = random.randint(100000, 999999)
                hash = hashlib.md5(str(pin).encode('utf-8')).hexdigest()
                hash = base64.b32encode(bytearray(settings.SECRET_KEY + hash, 'ascii')).decode('utf-8')
                new_pin = Pin(pin=pin, secret=hash)
                new_pin.save()
                print(pin)
            return redirect('/admin/pin/pin/')
        
        return render(request, 'change_form.html')
        

