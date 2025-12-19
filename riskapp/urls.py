from django.urls import path
from . import views

urlpatterns = [
path('', views.add_customer, name='add_customer'),
path('customers/', views.customers, name='customers'),
]
