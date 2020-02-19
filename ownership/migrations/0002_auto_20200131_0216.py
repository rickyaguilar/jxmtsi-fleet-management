# Generated by Django 2.1.7 on 2020-01-31 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='TOO_SLA',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='approved_by_jd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='cond_sticker',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='confirmation_status',
            field=models.CharField(blank=True, choices=[('Confirmed', 'Confirmed'), ('Final Pay', 'Final Pay')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='date_application',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='date_comletion_vismin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='date_docs_return',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='date_notarized',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='date_pulled',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='date_transfered_completed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='deed_signed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='deedofsale_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='doc_date_completed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='emailed_to_casher',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='endorosed_to_insurance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='forwarded_fleet_liason',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='forwarded_to_liason',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='lto_date_in',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='lto_date_out',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='lto_date_return',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='plate_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='purpose',
            field=models.CharField(blank=True, choices=[('Deceased', 'Deceased'), ('Early Availment', 'Early Availment'), ('End of Car Plan', 'End of Car Plan'), ('FSSV Availment', 'FSSV Availment'), ('Promotion', 'Promotion'), ('Resigned', 'Resigned'), ('Shift from Non-Sales to Sales', 'Shift from Non-Sales to Sales'), ('Shift from Sales to Non-Sales', 'Shift from Sales to Non-Sales'), ('Winning Bidder', 'Winning Bidder')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='received_from_casher',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='req_Fname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='req_Lname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='req_band',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='req_cost',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='req_employee_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='req_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='requested_for_pullout',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='return_endorsementfleet',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='return_fleet_admin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='routed_to_jd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='tmg_date_in',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='tmg_date_out',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='tmg_date_return',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='transfer_fee',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='v_band',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='v_employee_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='v_fname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='v_lname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='vehicle_brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='vehicle_make',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='vehicle_model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='vendor',
            field=models.CharField(blank=True, choices=[('Globe Telecome', 'Globe Telecome'), ('Innove', 'Innove'), ('Bayantel Communication', 'Bayantel Communication')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ownership',
            name='vendor_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]