# Generated by Django 5.0.1 on 2024-05-08 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_app', '0006_remove_payslip_id_number_payslip_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payslip',
            name='employee',
        ),
    ]