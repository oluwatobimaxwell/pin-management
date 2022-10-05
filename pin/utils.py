import random
# from .models import Pin
def generate_pin(amount):
    for i in range(0, amount):
        pin = random.randint(100000, 999999)
        return(pin)


# def get_amount():
#     field_name = 'amount'
#     obj = Pin.objects.first()
#     field_object = Pin._meta.get_field(field_name)
#     field_value = field_object.value_from_object(obj)
#     print(field_value)
