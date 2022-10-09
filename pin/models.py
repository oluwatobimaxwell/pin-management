from django.db import models
import uuid

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
    secret = models.CharField(max_length=200, null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status=models.CharField(max_length=20, choices=STATUS, default="valid")
    pin = models.IntegerField( blank=True, null=True, editable=False)
    caller = models.ForeignKey(Caller, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.pin)

    



