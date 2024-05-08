from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee, Payslip

import calendar
month_to_int = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}

# Create your views here.
'''
All querysets done here.
Creating Data Records: The django application receives the data from the form through a function in views.py and prepares it for inputting to the database. 
'''

employees = Employee.objects.all()
payslips = Payslip.objects.all()

def home(request):
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
        'payslips': Payslip.objects.all(),
        'employees': Employee.objects.all()
    }

    if request.method == "POST":
        
        #data obtained from form
        employee_id = request.POST.get('payslip_employee')
        month = request.POST.get('payslip_date')
        month_int = month_to_int.get(month, None)
        year = request.POST.get('payslip_year')
        pay_cycle = int(request.POST.get('payslip_cycle'))

        if employee_id == 'ALL':
            employees = Employee.objects.all()
        else:
            employees = [Employee.objects.get(pk=employee_id)]

        for employee in employees:
            last_day = calendar.monthrange(int(year), int(month_int))[1]
            if pay_cycle == 1:
                date_range = f'{month} 1-{last_day//2}, {year}'
                tot_pay_no_tax = (0.5 * employee.rate) + (employee.allowance or 0) + (employee.overtime_pay or 0) - 100
            elif pay_cycle == 2:
                date_range = f'{month} {last_day//2 + 1}-{last_day}, {year}'
                tot_pay_no_tax = (0.5 * employee.rate) + (employee.allowance or 0) + (employee.overtime_pay or 0) - (employee.rate*0.045) - (employee.rate*0.04)
            else:
                # Add error handling
                pass

            tax = 0.2 * tot_pay_no_tax

            payslip = Payslip.objects.create(
                employee=employee,
                month=month,
                date_range=date_range,
                year=year,
                pay_cycle=1,
                rate=0.5 * employee.rate,
                earnings_allowance=employee.allowance or 0,
                deductions_tax=tax,
                deductions_health=0,
                pag_ibig=100,
                sss=0,
                overtime=employee.overtime_pay or 0,
                total_pay=tot_pay_no_tax - tax
            )

        return redirect('payslips')

    return render(request, 'payroll_app/payslips.html', context)

def view_payslip(request):
    #payslip = get_object_or_404(Payslip,pk=pk)
    return render(request,'payroll_app/view_payslip.html') #add context later

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



