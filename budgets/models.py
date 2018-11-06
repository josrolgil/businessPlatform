from django.db import models
from django.forms import ModelForm

from clients.models import Client
# Create your models here.


class Address(models.Model):
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

class DownloadAddress(models.Model):
    address1 = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='%(class)s_first_address')
    address2 = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='%(class)s_second_address') #todo: list?
    license = models.BooleanField()
    license_type = models.CharField(max_length=400)
    moving_date = models.DateField()
    visiting_date = models.DateField()
    confirmation = models.CharField(max_length=200)

class LoadAddress(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    license = models.BooleanField()
    license_type = models.CharField(max_length=400)

class Bedroom(models.Model):
    bed = models.IntegerField()
    wardrobe  = models.IntegerField()
    mirror  = models.IntegerField()
    commode  = models.IntegerField()
    bedsite_table  = models.IntegerField()
    chair  = models.IntegerField()
    cradle  = models.IntegerField()
    tv  = models.IntegerField()
    picture  = models.IntegerField()
    gym  = models.IntegerField()
    nest  = models.IntegerField()
    ark  = models.IntegerField()
    bridge  = models.IntegerField()
    desk  = models.IntegerField()
    rack  = models.IntegerField()
    shelves  = models.IntegerField()

class Dinningroom(models.Model):
    table  = models.IntegerField()
    chair  = models.IntegerField()
    module = models.IntegerField()
    wall  = models.IntegerField()
    entrance  = models.IntegerField()
    sofa  = models.IntegerField()
    center_table  = models.IntegerField()
    lamp  = models.IntegerField()
    showcase  = models.IntegerField()
    tv  = models.IntegerField()
    picture  = models.IntegerField()
    mirror  = models.IntegerField()
    low_furniture  = models.IntegerField()
    sideboard  = models.IntegerField()
    rack  = models.IntegerField()
    shelves  = models.IntegerField()

class Budget(models.Model):
    loadAddress = models.ForeignKey(LoadAddress, on_delete=models.CASCADE)
    downloadAddress = models.ForeignKey(DownloadAddress, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'
