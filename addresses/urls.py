from django.urls import path
from . import views
app_name = 'addresses'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_address, name='new_address'),
    path('edit/<int:address_id>', views.update_address, name='update_address'),
    path('delete/<int:address_id>', views.delete_address, name='delete_address'),
    path('detail/<int:address_id>', views.detail_address, name='detail_address'),

]