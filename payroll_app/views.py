from django.shortcuts import render
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
    return render(request, 'payroll_app/payslips.html', context)

def update_employee(request):
    pass

def generate_payslip(request):
    # generates two payslips 
    if request.method == 'POST':
        return render(request, 'payroll/payslips.html')
    
def view_payslip(request):
    return render(request,'payroll/view_payslip.html')

    