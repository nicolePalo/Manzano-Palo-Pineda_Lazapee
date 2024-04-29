# Generated by Django 5.0.1 on 2024-04-29 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=20)),
                ('rate', models.FloatField()),
                ('overtime_pay', models.FloatField(null=True)),
                ('allowance', models.FloatField(verbose_name=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('date_range', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
                ('pay_cycle', models.IntegerField()),
                ('rate', models.FloatField()),
                ('earnings_allowance', models.FloatField()),
                ('deductions_tax', models.FloatField()),
                ('deductions_health', models.FloatField()),
                ('pag_ibig', models.FloatField()),
                ('sss', models.FloatField()),
                ('overtime', models.FloatField()),
                ('total_pay', models.FloatField()),
                ('id_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payroll_app.employee')),
            ],
        ),
    ]
