from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee, Payslip

# Create your views here.
'''
All querysets done here.
Creating Data Records: The django application receives the data from the form through a function in views.py and prepares it for inputting to the database. 
'''

employees = Employee.objects.all()
payslip = Payslip.objects.all()

def home(request):
    context = {
        'nav_selected': 'Employees' 
    }
    return render(request, 'payroll_app/home.html', context)


def create_employee(request):
    pass

def payslips(request):
    context = {
        'nav_selected': 'Payslips',
        payslip:'payslips'
    }

    if request.method == "POST":
        employee = request.POST.get('payslip_employee')
        month = request.POST.get('payslip_month')
        year = request.POST.get('payslip_year')
        cycle = request.POST.get('payslip_cycle')

        if Payslip.objects.filter(employee=employee).exists():
            messages.error(request, "Employee already has payslip.")
            return render(request, 'payroll_app/payslips.html', context)
        else: 
            id_number = get_object_or_404(Employee,pk=employee)

            # Cycle 1 payslip
            Payslip.objects.create(
                id_number=id_number,
                month=month,
                date_range='',
                year=year,
                cycle=1
            )

            #Cycle 2 payslip
            Payslip.objects.create(
                id_number=id_number,
                cycle=2
            )
                
    else: 
        return render(request, 'payroll_app/payslips.html', context)

def update_employee(request):
    pass
    
def view_payslip(request, pk):
    payslip = get_object_or_404(Payslip,pk=pk)
    return render(request,'payroll/view_payslip.html', {payslip:'payslip'})