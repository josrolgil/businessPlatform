from django.urls import path
from . import views
app_name = 'budgets'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_budget, name='new_budget')
    # path('edit/<int:client_id>', views.update_client, name='update_client'),
    # path('delete/<int:client_id>', views.delete_client, name='delete_client'),
    # path('detail/<int:client_id>', views.detail_client, name='detail_client'),
]
