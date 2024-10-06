# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # You can add more fields as needed, for example:
    founded_year = models.IntegerField(null=True, blank=True)  # Year the make was founded
    def __str__(self):
        return self.name  


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')  # Many-to-one relationship
    dealer_id = models.IntegerField()  # Refers to a dealer in Cloudant database
    name = models.CharField(max_length=100)
    TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('wagon', 'Wagon'),
        # Add more choices as needed
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    year = models.DateField()
    # You can add more fields as needed, for example:
    color = models.CharField(max_length=30, null=True, blank=True)  # Color of the car

    def __str__(self):
        return f"{self.car_make.name} {self.name}"  # Return the make and model as the string representation