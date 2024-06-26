# Generated by Django 5.0.1 on 2024-05-08 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_app', '0007_remove_payslip_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payslip',
            name='date_range',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='deductions_health',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='deductions_tax',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='earnings_allowance',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='month',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='overtime',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='pag_ibig',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='pay_cycle',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='sss',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='total_pay',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='year',
        ),
    ]
