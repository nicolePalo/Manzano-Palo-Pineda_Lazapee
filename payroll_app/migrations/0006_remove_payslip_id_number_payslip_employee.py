# Generated by Django 5.0.1 on 2024-05-08 02:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_app', '0005_merge_20240507_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payslip',
            name='id_number',
        ),
        migrations.AddField(
            model_name='payslip',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='payroll_app.employee'),
            preserve_default=False,
        ),
    ]
