import json

from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect

from addresses.models import Address
from clients.models import Client
from .models import Budget, BudgetForm

# Create your views here.


def index(request):
    budgets = Budget.objects.order_by('id')
    context = {'budgets': budgets}
    return render(request, 'budgets/index.html', context)

def detail_budget(request, budget_id):
    pass

def  new_budget(request):
    form = BudgetForm(request.POST or None)
    clients = Client.objects.order_by('id')
    addresses = Address.objects.filter(client_id=clients[0].id).order_by('id')
    addresses=serializers.serialize("json", addresses)
    if form.is_valid():
        form.save()
        return redirect('budgets:index')
    return render(request, 'budgets/form.html', {'budget': form, 'clients': clients, 'addresses': addresses})

def update_budget(request, budget_id):
    pass

def delete_budget(request, budget_id):
    pass

def load_clients(request):
    clients = Client.object.order_by('id')
    context = {'clients': clients}
    return render(request)