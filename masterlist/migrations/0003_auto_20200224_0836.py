# Generated by Django 2.1.7 on 2020-02-24 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0002_auto_20200224_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalvehiclemasterlist',
            name='CS_NO',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclemasterlist',
            name='CS_NO',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
