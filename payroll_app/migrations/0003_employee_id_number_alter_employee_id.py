# Generated by Django 5.0.1 on 2024-05-02 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_app', '0002_remove_employee_id_number_alter_employee_allowance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='id_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
