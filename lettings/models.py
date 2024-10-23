from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Here is the address model with its attributes below (and some examples)

    Args:
        number: 10
        street: Avenue Gustave Eiffel
        city: Paris
        state: Ile-de-France
        zip_code: 75007
        country_iso_code: 3166-1
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "addresses"


class Letting(models.Model):
    """
    Here is the letting model with its attributes below (and some examples)

    Args:
        title: receives the name of the contact to save
        address: receives the already saved address to associate with the contact

    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
