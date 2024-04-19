from django.shortcuts import render
from .models import Employee, Payslip

# Create your views here.
'''
All querysets done here.
Creating Data Records: The django application receives the data from the form through a function in views.py and prepares it for inputting to the database. 
'''

def home(request):
    return render(request, 'payroll_app/home.html')
# The above has been given as an example. 

def create_employee(request):
    pass

def payslips(request):
    return render(request, 'payroll_app/payslips.html')

def update_employee(request):
    pass

def view_payslip(request):
    if request.method == 'POST':
        pass
    return render(request,'payroll/view_payslip.html')

    