from django.db import models
from django.forms import ModelForm

from addresses.models import LoadAddress, DownloadAddress
from clients.models import Client
# Create your models here.

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
