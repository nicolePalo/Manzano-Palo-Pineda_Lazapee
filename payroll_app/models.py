from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField()
    id_number = models.CharField()
    rate = models.FloatField()

    #set as nullable
    overtime_pay = models.FloatField() 
    allowance = models.FloatField()

    def getName(self):
        pass
    
    def getID(self):
        pass

    def getRate(self):
        pass

    def getOvertime(self):
        pass

    def getAllowance(self):
        pass

    def __str__(self):
        pass

class Payslip(models.Model):
    id_number = models.ForeignKey()
    month = models.CharField()
    date_range = models.CharField()
    year = models.CharField()
    pay_cycle = models.IntegerField()
    rate = models.FloatField()
    earnings_allowance = models.FloatField()
    deductions_tax = models.FloatField()
    deductions_health = models.FloatField()
    pag_ibig = models.FloatField()
    sss = models.FloatField()
    overtime = models.FloatField()
    total_pay = models.FloatField()

    def getIDNumber(self):
        pass

    def getMonth(self):
        pass

    def getDate_range(self):
        pass

    def getYear(self):
        pass

    def getPay_cycle(self):
        pass

    def getRate(self):
        pass

    def getCycleRate(self):
        pass

    def getEarnings_allowance(self):
        pass

    def getDeductions_tax(self):
        pass

    def getDeductions_health(self):
        pass

    def getPag_ibig(self):
        pass

    def getSSS(self):
        pass

    def getOvertime(self):
        pass

    def getTotal_pay(self):
        pass

    def __str__(self):
        pass