from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Account"

    def __str__(self):
        return f"{self.username}"


class Address(models.Model):
    number_of_house = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return f"{self.number_of_house}, {self.street}, {self.district}, {self.city}, {self.country}"


class Fullname(models.Model):
    firstname = models.CharField(max_length=255)
    midname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Fullname"

    def __str__(self):
        return f"{self.lastname} {self.midname} {self.firstname}"


class Customer(models.Model):
    dob = models.DateField(default=date.today)
    phone = models.CharField(max_length=255)
    account = models.ForeignKey(Account, related_name='customer_account', on_delete=models.CASCADE)
    address = models.ForeignKey(Address, related_name='customer_address', on_delete=models.CASCADE)
    fullname = models.ForeignKey(Fullname, related_name='customer_fullname', on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Customer"

    def __str__(self):
        return f"{self.account} - {self.fullname}"
