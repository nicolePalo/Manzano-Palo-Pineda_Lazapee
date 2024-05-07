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
    employees = Employee.objects.all()
    context = {
        'nav_selected': 'Employees',
        'employees': employees
    }
    return render(request, 'payroll_app/home.html', context)


def create_employee(request):
    
    context = {
        'nav_selected': 'Employees',
        'employees': employees
    }
    if request.method=="POST":
        name = request.POST.get('name')
        id = request.POST.get('id')
        rate = request.POST.get('rate')
        allowance = request.POST.get('allowance')
        if Employee.objects.filter(id_number=id).exists():
            messages.error(request, 'The ID Number already exists.')
            
            return render(request, 'payroll_app/create_employee.html', context)
        
        elif allowance == "":
            Employee.objects.create(name=name, id_number=id, rate=rate, allowance=0, overtime_pay= 0)
            return redirect('home')
        else:
            Employee.objects.create(name=name, id_number=id, rate=rate, allowance=allowance, overtime_pay= 0)
            return redirect('home')
    else:
        return render(request, 'payroll_app/create_employee.html', context )
   
    

def payslips(request):
    context = {
        'nav_selected': 'Payslips',
        payslip:'payslips',
        'employees':employees
    }

    if request.method == "POST":
        employee = request.POST.get('payslip_employee')

        if employee == "All Employees":
            pass
        else:
            employee = get_object_or_404(Employee,pk=employee)
        
        month = request.POST.get('payslip_month')
        year = request.POST.get('payslip_year')
        cycle = request.POST.get('payslip_cycle')

        philhealth = 0.045*employee.rate
        sss = 0.040*employee.rate
        
        if cycle == 1:
            days = "1-15"
            tax = ((0.5*employee.rate) +employee.allowance + employee.overtime_pay - 100)*0.2
            pay = ((0.5*employee.rate) +employee.allowance + employee.overtime_pay - 100) - tax
        elif cycle == 2:
            days = "15-30"
            pagibig = 0
            tax = ((0.5*employee.rate) +employee.allowance + employee.overtime_pay - philhealth - sss )*0.2
            pay = ((0.5*employee.rate) +employee.allowance + employee.overtime_pay - philhealth - sss ) - tax
                
    else: 
        return render(request, 'payroll_app/payslips.html', context)

def update_employee(request, pk):
    
    employee = get_object_or_404(Employee, pk=pk)
    if request.method=="POST":
        name = request.POST.get('name')
        id = request.POST.get('id')
        rate = request.POST.get('rate')
        allowance = request.POST.get('allowance')
        if Employee.objects.filter(id_number=id).exists():
            messages.error(request, 'The ID Number already exists.')
            
            return render(request, 'payroll_app/update_employee.html', {'employee':employee} )
        
        elif allowance == "":
            Employee.objects.filter(pk=pk).update(name=name, id_number=id, rate=rate, allowance=0, overtime_pay= 0)
            return redirect('home')
        else:
            Employee.objects.filter(pk=pk).update(name=name, id_number=id, rate=rate, allowance=allowance, overtime_pay= 0)
            return redirect('home')
    else:
        return render(request, 'payroll_app/update_employee.html', {'employee':employee} )
    
def view_payslip(request, pk):
    payslip = get_object_or_404(Payslip,pk=pk)
    return render(request,'payroll/view_payslip.html', {payslip:'payslip'})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()

    return redirect('home')

def add_overtime(request, pk):
    if request.method=="POST":
        overtime_hours = request.POST.get('overtime-hours')
        employee = get_object_or_404(Employee, pk=pk)
        employee.add_overtime_hours(overtime_hours)
    return redirect('home')

