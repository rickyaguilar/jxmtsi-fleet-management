# Generated by Django 2.1.7 on 2019-11-11 02:03

from django.db import migrations, models
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20191025_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrental',
            name='Activity_id',
            field=models.CharField(default=payment.models.increment_Activity_id, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclepayment',
            name='Activity_id',
            field=models.CharField(default=payment.models.increment_Activity_id, max_length=20),
        ),
    ]
