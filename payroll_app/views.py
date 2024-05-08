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
        'payslips':Payslip.objects.all(),
        'employees':employees
    }

    if request.method == "POST":
        
        #data obtained from form
        employee_id = request.POST.get('payslip_employee')
        month = request.POST.get('payslip_date')
        year = request.POST.get('payslip_year')
        pay_cycle = int(request.POST.get('payslip_cycle'))

        employee = Employee.objects.get(pk=employee_id)

        if pay_cycle == 1:
            date_range = f'{month} 1-15, {year}'
            tot_pay_no_tax = (0.5 * employee.rate) + (employee.allowance or 0) + (employee.overtime_pay or 0) - 100
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
            return render(request, 'payroll_app/payslips.html', context)
        

        ''' NOT REVIEWED YET! I can try to review leter - ethan
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
        '''
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
    }
    payslip = get_object_or_404(Payslip,pk=pk)

    if payslip.pay_cycle == 1:
        deductions = ['Pag-ibig']
        deduct_values = [payslip.pag_ibig]

    if payslip.pay_cycle == 2:
        deductions = ['PhilHealth','SSS']
        deduct_values = [payslip.deductions_health,payslip.sss]

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



