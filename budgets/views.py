from django.shortcuts import render, get_object_or_404, redirect

from clients.models import Client
from .models import Budget, BudgetForm

# Create your views here.


def index(request):
    budgets = Budget.objects.order_by('id')
    context = {'budgets': budgets}
    return render(request, 'budgets/index.html', context)

def  new_budget(request):
    form = BudgetForm(request.POST or None)
    clients = Client.objects.order_by('id')
    if form.is_valid():
        form.save()
        return redirect('budgets:index')
    return render(request, 'budgets/form.html', {'budget': form, 'clients': clients})


def load_clients(request):
    clients = Client.object.order_by('id')
    context = {'clients': clients}
    return render(request)