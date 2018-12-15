from django.db import models
from django import forms
# Create your models here.
from django.forms import ModelForm

from clients.models import Client


class Address(models.Model):
    #ModelChoiceField
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    street = models.CharField(max_length=1000)
    number = models.IntegerField()
    building = models.CharField(max_length=100)
    door=models.CharField(max_length=100)
    elevator = models.BooleanField()
    terrace = models.BooleanField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    forklift = models.BooleanField()
    forklift_type = models.CharField(max_length=200)

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'