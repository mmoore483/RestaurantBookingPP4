from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    phone = PhoneNumberField()
    email = models.EmailField()


class Table(models.Model):
    table_id = models.AutoField(primary_key=True, unique=True)
    capacity = models.PositiveSmallIntegerField()
    available = models.BooleanField(default=True, verbose_name="Table Availability")


class Reservation(models.Model):
    booking_id = models.AutoField(primary_key=True, unique=True)
    partysize = models.PositiveSmallIntegerField()
    date = models.DateField(default=timezone.now)
    time_booking = models.TimeField()
    time_available = models.TimeField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)