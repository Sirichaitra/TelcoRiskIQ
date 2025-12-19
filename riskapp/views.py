from django.shortcuts import render, redirect
from .models import Customer


def add_customer(request):
    if request.method == 'POST':
        Customer.objects.create(
        name=request.POST['name'],
        mobile_number=request.POST['mobile'],
        monthly_bill=float(request.POST['bill'])
        )
        return redirect('customers')
    return render(request, 'add_customer.html')


def customers(request):
    data = Customer.objects.all()
    return render(request, 'customers.html', {'customers': data})
