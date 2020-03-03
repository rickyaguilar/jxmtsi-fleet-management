# Generated by Django 2.1.7 on 2020-03-03 01:44

from django.db import migrations, models
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalvehiclepayment',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vehiclepayment',
            name='invoice_number',
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
