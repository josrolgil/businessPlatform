import json

from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect

from addresses.models import Address
from clients.models import Client
from .models import Budget, BudgetForm, LoadAddressForm, LoadAddress, DownloadAddressForm, DownloadAddress


# Create your views here.


def index(request):

    budgets = Budget.objects.order_by('id')
    context = {'budgets': budgets}
    return render(request, 'budgets/index.html', context)

def detail_budget(request, budget_id):
    pass

def  new_budget(request):
    formBudget = BudgetForm(request.POST or None)
    formLoadAddress = LoadAddressForm(request.POST or None)
    formDownloadAddress = DownloadAddress(request.POST or None)
    clients = Client.objects.order_by('id')
    addresses = Address.objects.filter(client_id=clients[0].id).order_by('id')
    addresses_json=serializers.serialize("json", addresses)

    if request.method=='POST':
        load_address_form = LoadAddressForm(request.POST, instance=LoadAddress())
        download_address_form = DownloadAddressForm(request.POST, instance=DownloadAddress())
        budget_form = BudgetForm(request.POST, instance=Budget())
        if budget_form.is_valid() and load_address_form.is_valid() and download_address_form.is_valid():
            new_download_address = download_address_form.save()
            new_load_address = load_address_form.save()
            new_budget = budget_form.save(commit=False)
            new_budget.loadAddress = new_load_address
            new_budget.downloadAddress = new_download_address
            return redirect('budgets:index')
    #
    # if form.is_valid() and formLoad.is_valid():
    #     form.save()
    #     return redirect('budgets:index')
    return render(request, 'budgets/form.html', {'budget': formBudget,'load_address':formLoadAddress, 'download_address':formDownloadAddress, 'clients': clients, 'addresses': addresses, 'addresses_json':addresses_json})

def update_budget(request, budget_id):
    pass

def delete_budget(request, budget_id):
    pass

def load_clients(request):
    clients = Client.object.order_by('id')
    context = {'clients': clients}
    return render(request)