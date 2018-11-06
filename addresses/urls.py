from django.urls import path
from . import views
app_name = 'addresses'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_budget, name='new_address')

]