from django.db import models

# Create your models here.
from django.forms import ModelForm


class Client(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=400)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class ClientForm(ModelForm):
    class Meta:
        model = Client
        #fields = ['name', 'lastname', 'address', 'city']
        fields = '__all__'
