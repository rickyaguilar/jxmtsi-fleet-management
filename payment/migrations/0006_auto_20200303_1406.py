# Generated by Django 2.1.7 on 2020-03-03 06:06

from django.db import migrations, models
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20200303_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrental',
            name='car_provider',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carrental',
            name='rfp_no2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carrental',
            name='sqa_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalcarrental',
            name='car_provider',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalcarrental',
            name='rfp_no2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalcarrental',
            name='sqa_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carrental',
            name='Activity_id',
            field=models.CharField(default=payment.models.increment_Activity_id, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fuel_supplier',
            name='Activity_id',
            field=models.CharField(default=payment.models.increment_Activity_id, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcarrental',
            name='Activity_id',
            field=models.CharField(default=payment.models.increment_Activity_id, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfuel_supplier',
            name='Activity_id',
            field=models.CharField(default=payment.models.increment_Activity_id, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='historicalvehiclepayment',
            name='Activity_id',
            field=models.CharField(default=payment.models.increment_Activity_id, max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiclepayment',
            name='Activity_id',
            field=models.CharField(default=payment.models.increment_Activity_id, max_length=20),
        ),
    ]
