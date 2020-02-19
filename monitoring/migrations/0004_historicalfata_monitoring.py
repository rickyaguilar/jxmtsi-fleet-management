# Generated by Django 2.1.7 on 2020-02-18 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import monitoring.models
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitoring', '0003_auto_20200203_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalFata_monitoring',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_id', models.CharField(default=monitoring.models.increment_Activity_id, max_length=100)),
                ('Fata_no', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_transfer', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_received', models.CharField(blank=True, max_length=100, null=True)),
                ('Plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('Vehicle_make', models.CharField(blank=True, max_length=100, null=True)),
                ('Vehicle_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('Certificate_of_Reg', models.CharField(blank=True, max_length=100, null=True)),
                ('Vehicle_model', models.CharField(blank=True, max_length=100, null=True)),
                ('Transferor_employee', models.CharField(blank=True, max_length=100, null=True)),
                ('Transferor_Fname', models.CharField(blank=True, max_length=100, null=True)),
                ('Transferor_Lname', models.CharField(blank=True, max_length=100, null=True)),
                ('Recipient_Employee', models.CharField(blank=True, max_length=100, null=True)),
                ('Recipient_Fname', models.CharField(blank=True, max_length=100, null=True)),
                ('Recipient_Lname', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_endorsed_Globe', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_endorsed_Innove', models.CharField(blank=True, max_length=100, null=True)),
                ('Clearing_accountability', models.CharField(blank=True, max_length=10, null=True)),
                ('Globe_fixed_asset', models.CharField(blank=True, max_length=50, null=True)),
                ('Innove_fixed_asset', models.CharField(blank=True, max_length=50, null=True)),
                ('Date_initiated', models.DateField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical fata_monitoring',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
