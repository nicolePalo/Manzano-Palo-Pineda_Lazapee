from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee, Payslip


# Create your views here.
'''
All querysets done here.
Creating Data Records: The django application receives the data from the form through a function in views.py and prepares it for inputting to the database. 
'''

employees = Employee.objects.all()
payslips = Payslip.objects.all()

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
        'payslips':payslips,
        'employees':employees
    }

    if request.method == "POST":
        
        #data obtained from form. do not modify.
        id = request.POST.get('payslip_employee')
        month = request.POST.get('payslip_date')
        year = request.POST.get('payslip_year')
        pay_cycle = request.POST.get('payslip_cycle')
        #----------------------------------------------------------------------------------

        #So far didn't start coding for cases of "All Employees"
        employee = Employee.objects.filter(id_number=id)

        if pay_cycle == 1:
            date_range = f'{month} 1-15, {year}'
            Payslip.objects.create(id_number = id,
                                   month=month,
                                   date_range=date_range,
                                   year=year,
                                   pay_cycle=1,
                                   rate=0.5*employee.rate,
                                   earnings_allowance=employee.allowance,
                                   deductions_tax=0.2*((0.5*employee.rate)+employee.allowance+employee.overtime-100),
                                   deductions_health=0,
                                   pag_ibig=100,
                                   sss=0,
                                   overtime=employee.overtime_pay,
                                   total_pay=0.8*((0.5*employee.rate)+employee.allowance+employee.overtime-100))
            return redirect('payslips')

        if pay_cycle == 2:
            date_range = f'{month} 16-30, {year}'
            Payslip.objects.create(id_number = id,
                                   month=month,
                                   date_range=date_range,
                                   year=year,
                                   pay_cycle=1,
                                   rate= 0.5*employee.rate,
                                   earnings_allowance=employee.allowance,
                                   deductions_tax=0.2*((0.5*employee.rate)+employee.allowance+employee.overtime-0.04*employee.rate-0.045*employee.rate),
                                   deductions_health=0.04*employee.rate,
                                   pag_ibig=0,
                                   sss= 0.045*employee.rate,
                                   overtime=employee.overtime_pay,
                                   total_pay=0.8*((0.5*employee.rate)+employee.allowance+employee.overtime-0.04*employee.rate-0.045*employee.rate))
            return redirect('payslips')
        
        #debugging
        query = Payslip.objects.all()
        print(query)

        return render(request, 'payroll_app/payslips.html', context)
    else: 
        return render(request, 'payroll_app/payslips.html', context)

'''
def payslips(request):
    context = {
        'nav_selected': 'Payslips',
        'payslips': Payslip.objects.all(),
        'employees': Employee.objects.all()
    }

    if request.method == "POST":
        employee = request.POST.get('payslip_employee')
        if employee == "All Employees":
            payslips = Payslip.objects.all()
        else:
            employee = get_object_or_404(Employee, pk=employee)
            payslips = Payslip.objects.filter(id_number=employee.id_number)

        month = request.POST.get('payslip_month')
        year = request.POST.get('payslip_year')
        cycle = int(request.POST.get('payslip_cycle'))

        for payslip in payslips:
            philhealth = 0.045 * float(payslip.employee.rate)
            sss = 0.040 * float(payslip.employee.rate)

            if cycle == 1:
                days = "1-15"
                tax = ((0.5 * float(payslip.employee.rate)) + payslip.employee.allowance + payslip.employee.overtime_pay - 100) * 0.2
                pay = ((0.5 * float(payslip.employee.rate)) + payslip.employee.allowance + payslip.employee.overtime_pay - 100) - tax
            elif cycle == 2:
                days = "15-30"
                pagibig = 0
                tax = ((0.5 * float(payslip.employee.rate)) + payslip.employee.allowance + payslip.employee.overtime_pay - philhealth - sss) * 0.2
                pay = ((0.5 * float(payslip.employee.rate)) + payslip.employee.allowance + payslip.employee.overtime_pay - philhealth - sss) - tax

            Payslip.objects.create(days = days, philhealth = philhealth, sss=sss, tax=tax, pay=pay))
            
   
            payslip.days = days
            payslip.philhealth = philhealth
            payslip.sss = sss
            payslip.tax = tax
            payslip.net_pay = pay
            payslip.save()

    return render(request, 'payroll_app/payslips.html', context)
'''    

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



