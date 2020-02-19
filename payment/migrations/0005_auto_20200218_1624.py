# Generated by Django 2.1.7 on 2020-02-18 08:24

from django.db import migrations, models
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20200131_0240'),
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
