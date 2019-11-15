# Generated by Django 2.1.7 on 2019-11-14 07:17

from django.db import migrations, models
import django.db.models.deletion
import request.models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0005_auto_20191114_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrentalrequest',
            name='Activity_id',
            field=models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gas_card',
            name='Activity_id',
            field=models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service_vehicle',
            name='Activity_id',
            field=models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service_vehicle',
            name='E_plate_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='masterlist.VehicleMasterList'),
        ),
    ]