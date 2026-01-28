from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import EmployeeForm
from .models import Employee


def home(request):
    # A small piece of dynamic content (per the manual)
    context = {
        'title': 'Home Page',
        'message': 'Welcome to the Employee Management System',
    }
    return render(request, 'employees/home.html', context)


def about(request):
    return render(request, 'employees/about.html')


@login_required
def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employees/employee_list.html', {'employees': employees})


@login_required
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form, 'mode': 'add'})


@login_required
def update_employee(request, id: int):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form, 'mode': 'edit', 'employee': employee})


@login_required
def delete_employee(request, id: int):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})
