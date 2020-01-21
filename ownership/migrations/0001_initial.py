# Generated by Django 2.1.7 on 2020-01-20 06:34

from django.db import migrations, models
import django.db.models.deletion
import ownership.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masterlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=ownership.models.increment_Activity_id, max_length=100)),
                ('date_application', models.DateField(null=True)),
                ('req_employee_id', models.CharField(max_length=50, null=True)),
                ('req_Fname', models.CharField(max_length=100, null=True)),
                ('req_Lname', models.CharField(max_length=100, null=True)),
                ('req_band', models.CharField(max_length=100, null=True)),
                ('req_cost', models.CharField(max_length=100, null=True)),
                ('req_title', models.CharField(max_length=100, null=True)),
                ('cond_sticker', models.CharField(max_length=100, null=True)),
                ('vehicle_model', models.CharField(max_length=100, null=True)),
                ('vehicle_brand', models.CharField(max_length=100, null=True)),
                ('vehicle_make', models.CharField(max_length=100, null=True)),
                ('vendor', models.CharField(choices=[('Globe Telecome', 'Globe Telecome'), ('Innove', 'Innove'), ('Bayantel Communication', 'Bayantel Communication')], max_length=100, null=True)),
                ('vendor_name', models.CharField(max_length=100, null=True)),
                ('v_employee_id', models.CharField(max_length=100, null=True)),
                ('v_fname', models.CharField(max_length=100, null=True)),
                ('v_lname', models.CharField(max_length=100, null=True)),
                ('v_band', models.CharField(max_length=100, null=True)),
                ('purpose', models.CharField(choices=[('Deceased', 'Deceased'), ('Early Availment', 'Early Availment'), ('End of Car Plan', 'End of Car Plan'), ('FSSV Availment', 'FSSV Availment'), ('Promotion', 'Promotion'), ('Resigned', 'Resigned'), ('Shift from Non-Sales to Sales', 'Shift from Non-Sales to Sales'), ('Shift from Sales to Non-Sales', 'Shift from Sales to Non-Sales'), ('Winning Bidder', 'Winning Bidder')], max_length=100, null=True)),
                ('transfer_fee', models.CharField(max_length=100, null=True)),
                ('doc_date_completed', models.DateField(null=True)),
                ('deedofsale_date', models.DateField(null=True)),
                ('confirmation_status', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Final Pay', 'Final Pay')], max_length=100, null=True)),
                ('emailed_to_casher', models.DateField(null=True)),
                ('received_from_casher', models.DateField(null=True)),
                ('deed_signed', models.DateField(null=True)),
                ('routed_to_jd', models.DateField(null=True)),
                ('approved_by_jd', models.DateField(null=True)),
                ('return_fleet_admin', models.DateField(null=True)),
                ('forwarded_to_liason', models.DateField(null=True)),
                ('date_notarized', models.DateField(null=True)),
                ('endorosed_to_insurance', models.DateField(null=True)),
                ('requested_for_pullout', models.DateField(null=True)),
                ('date_pulled', models.DateField(null=True)),
                ('return_endorsementfleet', models.DateField(null=True)),
                ('forwarded_fleet_liason', models.DateField(null=True)),
                ('tmg_date_in', models.DateField(null=True)),
                ('tmg_date_out', models.DateField(null=True)),
                ('tmg_date_return', models.DateField(null=True)),
                ('lto_date_in', models.DateField(null=True)),
                ('lto_date_out', models.DateField(null=True)),
                ('lto_date_return', models.DateField(null=True)),
                ('date_docs_return', models.DateField(null=True)),
                ('date_transfered_completed', models.DateField(null=True)),
                ('date_comletion_vismin', models.DateField(null=True)),
                ('TOO_SLA', models.CharField(max_length=10, null=True)),
                ('date_initiated', models.DateField(auto_now=True, null=True)),
                ('plate_no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='masterlist.VehicleMasterList')),
            ],
        ),
    ]
