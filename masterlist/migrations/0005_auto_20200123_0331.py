# Generated by Django 2.1.7 on 2020-01-23 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0004_auto_20200123_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemasterlist',
            name='Employee_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='masterlist.EmployeeMasterlist'),
        ),
    ]
