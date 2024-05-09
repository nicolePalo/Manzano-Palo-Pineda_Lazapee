'''
We hereby attest to the truth of the following facts:

We have not discussed the HTML/CSS/Bootstrap/Python/Django language code in our program with anyone other than our instructor or the teaching assistants assigned to this course.

We have not used HTML/CSS/Bootstrap/Python/Django language code obtained from another student, or any other unauthorized source, either modified or unmodified

If any HTML/CSS/Bootstrap/Python/Django language code or docomentation used in our program was obtained from another source, such as a textbook or course notes, that has been clearly noted with a proper citation in the comments of our program.

Bootstrap. (n.d.). Navbar. Bootstrap. https://getbootstrap.com/docs/5.0/components/navbar/.
Bootstrap. (n.d.). Select. Bootstrap. https://getbootstrap.com/docs/5.0/forms/select/.
Bootstrap. (n.d.). Spacing. Bootstrap. https://getbootstrap.com/docs/5.0/utilities/spacing/.
Chapagain, S. (2023, July 6). How to Use a Foreign Key to Create Many-to-One Relationships in Django. Free Code Camp. https://www.freecodecamp.org/news/what-is-one-to-many-relationship-in-django/
Django. (n.d.). Many-to-one relationships. Django. https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_one/
pcoronel. (2014, May 19). Restrict django FloatField to 2 decimal places. Stack Overflow. https://stackoverflow.com/questions/23739030/restrict-django-floatfield-to-2-decimal-places.
W3Schools. (n.d.). CSS3 Borders. W3Schools. https://www.w3schools.com/css/css3_borders.asp.
W3Schools. (n.d.). CSS3 Images. W3Schools. https://www.w3schools.com/css/css3_images.asp.
W3Schools. (n.d.). CSS3 Shadows. W3Schools. https://www.w3schools.com/css/css3_shadows.asp.
W3Schools. (n.d.). CSS3 Text Justify. W3Schools. https://www.w3schools.com/cssref/css3_pr_text-justify.php.
W3Schools. (n.d.). CSS Text Spacing. W3Schools. https://www.w3schools.com/css/css_text_spacing.asp.
W3Schools. (n.d.). HTML <input> placeholder Attribute. W3Schools. https://www.w3schools.com/tags/att_input_placeholder.asp.
yuvi. (2013, October 28). django difference between - one to one, many to one and many to many. Stack Overflow. https://stackoverflow.com/questions/19641841/django-difference-between-one-to-one-many-to-one-and-many-to-many
'''

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

        if not request.POST.get('payslip_employee'):
            messages.error(request, "Please select an employee.")
            return redirect('payslips')  

        if not request.POST.get('payslip_date') or not request.POST.get('payslip_cycle'):
            messages.error(request, "Please select a month and pay cycle.")
            return redirect('payslips')
        
        if not request.POST.get('payslip_year'):
            messages.error(request, "Please input a year.")
            return redirect('payslips')
        

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
            
            #handles duplicates
            if Payslip.objects.filter(employee=employee,month=month,year=year,pay_cycle=pay_cycle).exists():
                messages.error(request,f'Failed to create payslip. Payslip already exists.')
                return render(request, 'payroll_app/payslips.html', context)

            else:

                last_day = calendar.monthrange(int(year), int(month_int))[1]
                if pay_cycle == 1:
                    date_range = f'{month} 1-{last_day//2}, {year}'
                    tot_pay_no_tax = (0.5 * employee.rate) + (employee.allowance or 0) + (employee.overtime_pay or 0) - 100
                    pag_ibig = 100
                    deductions_health = 0
                    sss=0
                elif pay_cycle == 2:
                    date_range = f'{month} {last_day//2 + 1}-{last_day}, {year}'
                    tot_pay_no_tax = (0.5 * employee.rate) + (employee.allowance or 0) + (employee.overtime_pay or 0) - (employee.rate*0.045) - (employee.rate*0.04)
                    pag_ibig = 0
                    deductions_health = employee.rate*0.04
                    sss=employee.rate*0.045
                else:
                    messages.error(request, f"Invalid pay cycle selected for employee.")
                    return render(request, 'payroll_app/payslips.html', context)

                tax = 0.2 * tot_pay_no_tax

                payslip = Payslip.objects.create(
                    employee=employee,
                    month=month,
                    date_range=date_range,
                    year=year,
                    pay_cycle=pay_cycle,
                    rate=0.5*employee.rate,
                    earnings_allowance=employee.allowance or 0,
                    deductions_tax=tax,
                    deductions_health=deductions_health,
                    pag_ibig=pag_ibig,
                    sss=sss,
                    overtime=employee.overtime_pay or 0,
                    total_pay=tot_pay_no_tax - tax
                )

                employee.resetOvertime()


        return redirect('payslips')
    return render(request, 'payroll_app/payslips.html', context)


def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method=="POST":
        name = request.POST.get('name')
        id = request.POST.get('id')
        rate = request.POST.get('rate')
        allowance = request.POST.get('allowance')
        if Employee.objects.filter(id_number=id).exists() and Employee.objects.filter(id_number=id) != employee.id_number:
            messages.error(request, 'The ID Number already exists.')
            return render(request, 'payroll_app/update_employee.html', {'employee':employee} )
        Employee.objects.filter(pk=pk).update(name=name, rate=rate, allowance=allowance or 0, overtime_pay= 0)
        return redirect('home')
    
    return render(request, 'payroll_app/update_employee.html', {'employee':employee} )
    
def view_payslip(request,pk):
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
        
    context={
        'payslip':payslip,
        'deductions':deductions,
        'deduct_values':deduct_values,
        'deduct_sum':deduct_sum,
        'earned_sum':earned_sum
    }
    return render(request,'payroll_app/view_payslip.html',context) 

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



