from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee, Payslip

import calendar
month_to_int = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}

# Create your views here.

def home(request):
    context = {
        'nav_selected': 'Employees',
        'employees': Employee.objects.all()
    }
    return render(request, 'payroll_app/home.html', context)

def create_employee(request):
    context = {
        'nav_selected': 'Employees',
        'employees': Employee.objects.all()
    }
    if request.method=="POST":
        name = request.POST.get('name')
        id_number = request.POST.get('id')
        rate = request.POST.get('rate')
        allowance = request.POST.get('allowance')

        if Employee.objects.filter(id_number=id_number).exists():
            messages.error(request, 'The ID Number already exists.')
            return render(request, 'payroll_app/create_employee.html', context)

        Employee.objects.create(
            name=name,
            id_number=id_number,
            rate=rate,
            allowance=allowance or 0,
            overtime_pay=0
        )
        return redirect('home')
    
    return render(request, 'payroll_app/create_employee.html', context )

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        name = request.POST.get('name')
        id_number = request.POST.get('id')
        rate = request.POST.get('rate')
        allowance = request.POST.get('allowance')

        if Employee.objects.filter(id_number=id_number).exists():
            messages.error(request, 'The ID Number already exists.')
            return render(request, 'payroll_app/update_employee.html', {'employee': employee})

        employee.name = name
        employee.id_number = id_number
        employee.rate = rate
        employee.allowance = allowance or 0
        employee.overtime_pay = 0
        employee.save()
        return redirect('home')

    return render(request, 'payroll_app/update_employee.html', {'employee': employee})

def payslips(request):
    context = {
        'nav_selected': 'Payslips',
        'payslips': Payslip.objects.all(),
        'employees': Employee.objects.all()
    }

    if request.method == "POST":
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
                pay_cycle=pay_cycle,
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
    
def view_payslip(request,pk):
    context={
        'payslip':payslip,
        'deductions':deductions,
        'deduct_values':deduct_values,
        'deduct_sum':deduct_sum,
        'earned_sum':earned_sum
    }
    payslip = get_object_or_404(Payslip,pk=pk)

    earned_sum = float(payslip.rate)+float(payslip.earnings_allowance)+float(payslip.overtime)

    if payslip.pay_cycle == 1:
        deductions = ['Pag-ibig']
        deduct_values = [payslip.pag_ibig]
        deduct_sum = float(payslip.deductions_tax)+float(payslip.pag_ibig)

    if payslip.pay_cycle == 2:
        deductions = ['PhilHealth','SSS']
        deduct_values = [payslip.deductions_health,payslip.sss]
        deduct_sum = float(payslip.deductions_tax)+float(payslip.deductions_health)+float(payslip.sss)

    return render(request,'payroll_app/view_payslip.html',context) #add context later

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



