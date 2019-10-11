# Generated by Django 2.1.7 on 2019-10-10 03:00

from django.db import migrations, models
import monitoring.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fata_monitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=monitoring.models.increment_Activity_id, max_length=100)),
                ('Fata_no', models.CharField(default=monitoring.models.increment_Fata_no, max_length=100)),
                ('Date_transfer', models.DateField(null=True)),
                ('Date_received', models.DateField()),
                ('Plate_no', models.CharField(max_length=50, null=True)),
                ('Vehicle_make', models.CharField(max_length=100, null=True)),
                ('Vehicle_brand', models.CharField(max_length=100, null=True)),
                ('Certificate_of_Reg', models.CharField(max_length=100, null=True)),
                ('Vehicle_model', models.CharField(max_length=100, null=True)),
                ('Transferor_employee', models.CharField(max_length=100, null=True)),
                ('Transferor_Fname', models.CharField(max_length=100, null=True)),
                ('Transferor_Lname', models.CharField(max_length=100, null=True)),
                ('Recipient_Employee', models.CharField(max_length=100, null=True)),
                ('Recipient_Fname', models.CharField(max_length=100, null=True)),
                ('Recipient_Lname', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]