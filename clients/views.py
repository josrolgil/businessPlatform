from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, ClientForm


def index(request):
    clients = Client.objects.order_by('id')
    context = {'clients': clients}
    return render(request, 'clients/index.html', context)

def detail_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'clients/detail.html', {'client':client})

def new_client(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clients:index')
    return render(request, 'clients/form.html', {'client': form})

def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('clients:index')
    return render(request, 'clients/form.html', {'form':form})

def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if(request.method=='POST'):
        client.delete()
        return redirect('clients:index')
    return render(request, 'clients/confirm_delete.html', {'object': client})

def login(request):
    return render(request, 'clients/login2.html')