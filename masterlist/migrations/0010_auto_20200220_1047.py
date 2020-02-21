# Generated by Django 2.1.7 on 2020-02-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterlist', '0009_historicalemployeemasterlist_historicalvehiclemasterlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemasterlist',
            name='External_role',
        ),
        migrations.RemoveField(
            model_name='employeemasterlist',
            name='Hiring_date',
        ),
        migrations.RemoveField(
            model_name='employeemasterlist',
            name='Job_category',
        ),
        migrations.RemoveField(
            model_name='employeemasterlist',
            name='Tenure',
        ),
        migrations.RemoveField(
            model_name='historicalemployeemasterlist',
            name='External_role',
        ),
        migrations.RemoveField(
            model_name='historicalemployeemasterlist',
            name='Hiring_date',
        ),
        migrations.RemoveField(
            model_name='historicalemployeemasterlist',
            name='Job_category',
        ),
        migrations.RemoveField(
            model_name='historicalemployeemasterlist',
            name='Tenure',
        ),
        migrations.AlterField(
            model_name='employeemasterlist',
            name='Middle_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='historicalemployeemasterlist',
            name='Middle_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]