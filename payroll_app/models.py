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
W3Schools. (n.d.). CSS3 Borders. W3Schools. https://www.w3schools.com/css/css3_borders.asp.
W3Schools. (n.d.). CSS3 Images. W3Schools. https://www.w3schools.com/css/css3_images.asp.
W3Schools. (n.d.). CSS3 Shadows. W3Schools. https://www.w3schools.com/css/css3_shadows.asp.
W3Schools. (n.d.). CSS3 Text Justify. W3Schools. https://www.w3schools.com/cssref/css3_pr_text-justify.php.
W3Schools. (n.d.). CSS Text Spacing. W3Schools. https://www.w3schools.com/css/css_text_spacing.asp.
W3Schools. (n.d.). HTML <input> placeholder Attribute. W3Schools. https://www.w3schools.com/tags/att_input_placeholder.asp.
yuvi. (2013, October 28). django difference between - one to one, many to one and many to many. Stack Overflow. https://stackoverflow.com/questions/19641841/django-difference-between-one-to-one-many-to-one-and-many-to-many
'''

from django.db import models

# Refer to project specs for parameters: https://docs.google.com/document/d/1r8DYEnlicUeXxNJ3uyP1WTNX55ikbRX2tyHNzPvoP1A/edit 

class Employee(models.Model):
    name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, unique=True)
    rate = models.FloatField()
    allowance = models.FloatField(null=True, blank=True)
    overtime_pay = models.FloatField(null=True, blank=True) 
    

    def __str__(self):
        return f"{self.pk}: {self.id_number}, rate: {self.rate}"
    
    def getName(self):
        return self.name
    
    def getID(self):
        return self.id_number

    def getRate(self):
        return self.rate

    def getOvertime(self):
        return self.overtime_pay
    
    def resetOvertime(self):
        self.overtime_pay = 0
        self.save()

    def getAllowance(self):
        return self.allowance
    
    def add_overtime_hours(self, overtime_hours):
        try:
            overtime_pay = (float(self.rate)/160) * 1.5 * float(overtime_hours)
            self.overtime_pay += overtime_pay
            self.save()
        except ValueError:
            print(f"Error: Invalid overtime hours for employee {self.name}")

class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    date_range = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    pay_cycle = models.IntegerField()
    rate = models.FloatField()
    earnings_allowance = models.FloatField()
    deductions_tax = models.FloatField()
    deductions_health = models.FloatField()
    pag_ibig = models.FloatField()
    sss = models.FloatField()
    overtime = models.FloatField()
    total_pay = models.FloatField()

    def __str__(self):
        return f"pk: {self.pk}, Employee: {self.employee.id_number}, Period: {self.month} {self.date_range}, {self.year}, Cycle: {self.pay_cycle}, Total Pay: {self.total_pay}"
    
    def getIDNumber(self):
        return self.employee.id_number

    def getMonth(self):
        return self.month

    def getDate_range(self):
        return self.date_range

    def getYear(self):
        return self.year

    def getPay_cycle(self):
        return self.pay_cycle

    def getRate(self):
        return self.rate

    def getCycleRate(self):
        return self.rate/2

    def getEarnings_allowance(self):
        return self.earnings_allowance

    def getDeductions_tax(self):
        return self.deductions_tax

    def getDeductions_health(self):
        return self.deductions_health

    def getPag_ibig(self):
        return self.pag_ibig

    def getSSS(self):
        return self.sss

    def getOvertime(self):
        return self.overtime

    def getTotal_pay(self):
        return self.total_pay