import random
from django.db import models
from django.forms import IntegerField
import uuid
from .utils import generator
from django.contrib.auth.models import User



def get_amount():
        field_name = 'amount'
        obj = Pin.objects.first()
        field_object = Pin._meta.get_field(field_name)
        field_value = field_object.value_from_object(obj)
        return(field_value)

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True)
    phone = models.CharField(max_length = 100, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Caller(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length = 200, blank=True, null=True)
    phone = models.CharField(max_length = 100, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
   
    def __str__(self):
        return str(self.name)

   

STATUS = (
    ("valid", "UNUSED"),
    ("invalid", "USED")
)
class Pin(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    secret = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=20, choices=STATUS, default="valid")
    pin = models.IntegerField( blank=True, null=True)
    caller = models.ForeignKey(Caller, on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     return str(self.pin)

    
    

    # def generate_pin():
    #     not_unique = True
    #     while not_unique:
    #         pin = random.randint(100000, 999999)
    #         if not Pin.objects.filter(pin=pin):
    #             not_unique = False
    #     return str(pin)
        



