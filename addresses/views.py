from django.shortcuts import render, get_object_or_404, redirect

from clients.models import Client
from .models import Address, DownloadAddress, LoadAddress, AddressForm


# Create your views here.
def index(request):
    addresses = Address.objects.order_by('id')
    context = {'addresses': addresses}
    return render(request, 'addresses/index.html', context)


def new_address(request):
    form = AddressForm(request.POST or None)
    clients = Client.objects.order_by('id')
    if form.is_valid():
        form.save()
        return redirect('addresses:index')
    return render(request, 'addresses/form.html', {'address': form, 'clients': clients})

def update_address(request, address_id):
    address = get_object_or_404(Address, pk=address_id)
    form = AddressForm(request.POST or None, instance=address)
    test = form.fields

    clients = Client.objects.order_by('id')
    if form.is_valid():
        form.save()
        return redirect('addresses:index')
    return render(request, 'addresses/form.html', {'form':form, 'clients': clients, 'selected_client_id': address.client.id})

def delete_address(request, address_id):
    address = get_object_or_404(Address, pk=address_id)
    if(request.method=='POST'):
        address.delete()
        return redirect('addresses:index')
    return render(request, 'addresses/confirm_delete.html', {'object':address})
