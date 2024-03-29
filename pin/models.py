from django.db import models
from django.core.exceptions import ValidationError
import uuid

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True)
    phone = models.CharField(max_length = 100, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


GENDER = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
)

class Caller(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length = 200, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, choices=GENDER)
    education = models.CharField(max_length=200, blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)
    management = models.CharField(max_length=200, blank=True, null=True)
    occupation = models.CharField(max_length=200, blank=True, null=True)
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

VALUE_CHOICES = (
    (100, "NGN 100"),
    (200, "NGN 200"),
    (300, "NGN 300"),
    (400, "NGN 400"),
    (500, "NGN 500"),
)

class Pin(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    is_cleaned = False
    secret = models.CharField(max_length=200, null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status=models.CharField(max_length=20, choices=STATUS, default="valid")
    pin = models.IntegerField( blank=True, null=True, editable=False)
    caller = models.ForeignKey(Caller, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True, editable=False)
    batch = models.IntegerField(default=0, null=True, blank=True, editable=False)
    value = models.IntegerField(default=100, blank=True, null=True, choices=VALUE_CHOICES)
    def __str__(self):
        return str(self.pin)
    
    def clean(self):
        self.is_cleaned = True
        if self._state.adding == False and Pin.objects.get(pk=self.pk).status == 'invalid':
            raise ValidationError(f'{self.pin} has already been used!')
        super(Pin, self).clean()

    
    def save(self, *args, **kwargs,):
        if not self.is_cleaned:
            self.full_clean()
        super(Pin, self).save(*args, **kwargs)
    



