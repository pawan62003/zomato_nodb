from django.db import models

# Create your models here.
class dish:
    def __init__(self,dish_name,price,availablety):
        self.dish_name = dish_name
        self.price = price
        self.availablety = availablety