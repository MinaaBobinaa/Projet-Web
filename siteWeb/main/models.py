from django.db import models
from .storage import UniqueFileSystemStorage


# Create an instance of your custom storage
unique_storage = UniqueFileSystemStorage()

# Create your models here.

class House(models.Model):
    HOUSE_TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('loft', 'Loft'),
        ('studio', 'Studio'),
    ]

    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=HOUSE_TYPE_CHOICES)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='houses/')  # Ensure you have Pillow installed to handle images ('python -m pip install Pillow' dans terminal )

    def __str__(self):
        return self.title
