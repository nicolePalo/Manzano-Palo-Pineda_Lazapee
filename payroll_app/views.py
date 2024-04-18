from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'payroll_app/home.html')

def create_employee(request):
    pass

def payslips(request):
    pass

def update_employee(request):
    pass

def view_payslip(request):
    pass