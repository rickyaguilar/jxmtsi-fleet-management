# Generated by Django 2.1.7 on 2020-01-16 04:52

from django.db import migrations, models
import django.db.models.deletion
import report.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masterlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=report.models.increment_Activity_id, max_length=100, null=True)),
                ('received_date', models.DateField(null=True)),
                ('v_accident_type', models.CharField(max_length=100, null=True)),
                ('support_docs', models.CharField(max_length=100, null=True)),
                ('v_model', models.CharField(max_length=100, null=True)),
                ('v_make', models.CharField(max_length=100, null=True)),
                ('cond_sticker', models.CharField(max_length=100, null=True)),
                ('a_employee_fname', models.CharField(max_length=100, null=True)),
                ('a_employee_lname', models.CharField(max_length=100, null=True)),
                ('a_employee_no', models.CharField(max_length=100, null=True)),
                ('a_employee_company', models.CharField(max_length=100, null=True)),
                ('a_employee_group', models.CharField(max_length=100, null=True)),
                ('a_employee_division', models.CharField(max_length=100, null=True)),
                ('a_employee_dept', models.CharField(max_length=100, null=True)),
                ('sup_employee_id', models.CharField(max_length=100, null=True)),
                ('sup_employee_fname', models.CharField(max_length=100, null=True)),
                ('sup_employee_lname', models.CharField(max_length=100, null=True)),
                ('inform_assignee', models.DateField(null=True)),
                ('date_of_inspection', models.DateField(null=True)),
                ('inspection_remarks', models.CharField(max_length=100, null=True)),
                ('date_filed_alarm', models.DateField(null=True)),
                ('date_cert_received', models.DateField(null=True)),
                ('date_forwarded', models.DateField(null=True)),
                ('date_initiated', models.DateField(auto_now=True, null=True)),
                ('MVAR_SLA', models.CharField(max_length=10, null=True)),
                ('a_employee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='masterlist.EmployeeMasterlist')),
                ('plate_number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='masterlist.VehicleMasterList')),
            ],
        ),
    ]
