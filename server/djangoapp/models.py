from django.db import models
from django.utils.timezone import now


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    description = models.CharField(null=False, max_length=1000, default='')

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}"


class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
    ]

    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='')
    dealer_id = models.IntegerField(null=True)
    type = models.CharField(null=False, max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.DateField(null=True)

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Year: {self.year}"
