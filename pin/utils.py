import random
# from .models import Pin
def generator(amount):
    for i in range(0, int(amount)):
        pin = random.randint(100000, 999999)
        print(pin)
