# Generated by Django 2.1.7 on 2020-03-03 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import request.models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarRentalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('A_Employee', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_received', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Fname', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Lname', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_No', models.CharField(blank=True, max_length=50, null=True)),
                ('Assignee_Company', models.CharField(blank=True, max_length=200, null=True)),
                ('Assignee_band', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Dept', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Cost', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Div', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Loc', models.CharField(blank=True, max_length=200, null=True)),
                ('Assignee_Section', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Designation', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_ATD', models.CharField(blank=True, max_length=100, null=True)),
                ('Vendor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.CharField(blank=True, max_length=100, null=True)),
                ('Up_to', models.CharField(blank=True, max_length=100, null=True)),
                ('Time', models.CharField(blank=True, max_length=100, null=True)),
                ('Place_of_del', models.CharField(blank=True, max_length=100, null=True)),
                ('type_rental', models.CharField(blank=True, choices=[('Daily', 'Daily'), ('Monthly', 'Monthly')], max_length=50, null=True)),
                ('Cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('Rental_period', models.CharField(blank=True, max_length=100, null=True)),
                ('Destination', models.CharField(blank=True, max_length=100, null=True)),
                ('Delivery_date', models.CharField(blank=True, max_length=100, null=True)),
                ('End_user', models.CharField(blank=True, max_length=100, null=True)),
                ('Type_of_vehicle', models.CharField(blank=True, choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('VAN', 'VAN')], max_length=50, null=True)),
                ('Plate_no', models.CharField(blank=True, max_length=50, null=True)),
                ('Immediate_supervisor', models.CharField(blank=True, choices=[('Ser Roy DelaCruz', 'Ser Roy DelaCruz'), ('Adolfo Carlos Umali', 'Adolfo Carlos Umali')], max_length=50, null=True)),
                ('CR_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('Date_initiated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gas_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('date_received', models.CharField(blank=True, max_length=100, null=True)),
                ('application_type', models.CharField(blank=True, choices=[('Daily', 'Daily'), ('Transfer Acountability', 'Transfer Acountability'), ('Cancel - Disposal of Vehicle', 'Cancel - Disposal of Vehicle'), ('Cancel - Resignation of User', 'Cancel - Resignation of User'), ('Replacement - Damage', 'Replacement - Damage'), ('Replacement - Lose', 'Replacement - Lose'), ('Others - Adjust Credit Limit', 'Others - Adjust Credit Limit'), ('Others - Change of Product Restriction', 'Others - Change of Product Restriction'), ('Others - Update Cost Center', 'Others - Update Cost Center')], max_length=100, null=True)),
                ('fleet_provider', models.CharField(blank=True, choices=[('Petron', 'Petron'), ('Shell', 'Shell')], max_length=100, null=True)),
                ('fleetcard_type', models.CharField(blank=True, choices=[('Single', 'Single'), ('Driver', 'Driver'), ('Vehicle', 'Vehicle')], max_length=100, null=True)),
                ('fuel_limit_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('fuel_limit_quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('products_restriction', models.CharField(blank=True, choices=[('S: Super Only', 'S: Super Only'), ('U: Super Unleaded Only', 'U: Super Unleaded Only'), ('R: Regular Only', 'R: Regular Only'), ('X: Velocity', 'X: Velocity'), ('D: Diesoline Only', 'D: Diesoline Only'), ('L: Lubricant Only', 'L: Lubricant Only'), ('V: Service Only', 'V: Service Only'), ('C: Convenience store items, sundries, accesories', 'C: Convenience store items, sundries, accesories')], max_length=100, null=True)),
                ('req_employee', models.CharField(blank=True, max_length=100, null=True)),
                ('req_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('req_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('req_title', models.CharField(blank=True, max_length=100, null=True)),
                ('req_cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('atd_no', models.CharField(blank=True, max_length=100, null=True)),
                ('temporary_atd', models.CharField(blank=True, max_length=100, null=True)),
                ('new_emp_id', models.CharField(blank=True, max_length=100, null=True)),
                ('new_emp_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('new_emp_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('new_emp_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('new_temp_atd', models.CharField(blank=True, max_length=100, null=True)),
                ('new_assignee', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_center_code', models.CharField(blank=True, max_length=100, null=True)),
                ('cancellation', models.CharField(blank=True, choices=[('Disposal Of Vehicle', 'Disposal Of Vehicle'), ('Resignation of User', 'Resignation of User')], max_length=100, null=True)),
                ('plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('con_sticker', models.CharField(blank=True, max_length=100, null=True)),
                ('model_year', models.CharField(blank=True, max_length=100, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('make', models.CharField(blank=True, max_length=100, null=True)),
                ('fuel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('new_plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('new_cond_sticker', models.CharField(blank=True, max_length=100, null=True)),
                ('new_model_year', models.CharField(blank=True, max_length=100, null=True)),
                ('new_vbrand', models.CharField(blank=True, max_length=100, null=True)),
                ('new_vmake', models.CharField(blank=True, max_length=100, null=True)),
                ('new_vfuel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('approved_by', models.CharField(blank=True, choices=[('Ser Roy Perluval Dela Cruz', 'Ser Roy Perluval Dela Cruz')], max_length=100, null=True)),
                ('date_summitted', models.CharField(blank=True, max_length=100, null=True)),
                ('fleet_received', models.CharField(blank=True, max_length=100, null=True)),
                ('fleet_card_no', models.CharField(blank=True, max_length=100, null=True)),
                ('fleet_date_release', models.CharField(blank=True, max_length=100, null=True)),
                ('person_release', models.CharField(blank=True, max_length=100, null=True)),
                ('date_initiated', models.DateField(auto_now=True)),
                ('GCR_SLA', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCarRentalRequest',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('A_Employee', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_received', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Fname', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Lname', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_No', models.CharField(blank=True, max_length=50, null=True)),
                ('Assignee_Company', models.CharField(blank=True, max_length=200, null=True)),
                ('Assignee_band', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Dept', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Cost', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Div', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Loc', models.CharField(blank=True, max_length=200, null=True)),
                ('Assignee_Section', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_Designation', models.CharField(blank=True, max_length=100, null=True)),
                ('Assignee_ATD', models.CharField(blank=True, max_length=100, null=True)),
                ('Vendor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.CharField(blank=True, max_length=100, null=True)),
                ('Up_to', models.CharField(blank=True, max_length=100, null=True)),
                ('Time', models.CharField(blank=True, max_length=100, null=True)),
                ('Place_of_del', models.CharField(blank=True, max_length=100, null=True)),
                ('type_rental', models.CharField(blank=True, choices=[('Daily', 'Daily'), ('Monthly', 'Monthly')], max_length=50, null=True)),
                ('Cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('Rental_period', models.CharField(blank=True, max_length=100, null=True)),
                ('Destination', models.CharField(blank=True, max_length=100, null=True)),
                ('Delivery_date', models.CharField(blank=True, max_length=100, null=True)),
                ('End_user', models.CharField(blank=True, max_length=100, null=True)),
                ('Type_of_vehicle', models.CharField(blank=True, choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('VAN', 'VAN')], max_length=50, null=True)),
                ('Plate_no', models.CharField(blank=True, max_length=50, null=True)),
                ('Immediate_supervisor', models.CharField(blank=True, choices=[('Ser Roy DelaCruz', 'Ser Roy DelaCruz'), ('Adolfo Carlos Umali', 'Adolfo Carlos Umali')], max_length=50, null=True)),
                ('CR_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('Date_initiated', models.DateField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical car rental request',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalGas_card',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('date_received', models.CharField(blank=True, max_length=100, null=True)),
                ('application_type', models.CharField(blank=True, choices=[('Daily', 'Daily'), ('Transfer Acountability', 'Transfer Acountability'), ('Cancel - Disposal of Vehicle', 'Cancel - Disposal of Vehicle'), ('Cancel - Resignation of User', 'Cancel - Resignation of User'), ('Replacement - Damage', 'Replacement - Damage'), ('Replacement - Lose', 'Replacement - Lose'), ('Others - Adjust Credit Limit', 'Others - Adjust Credit Limit'), ('Others - Change of Product Restriction', 'Others - Change of Product Restriction'), ('Others - Update Cost Center', 'Others - Update Cost Center')], max_length=100, null=True)),
                ('fleet_provider', models.CharField(blank=True, choices=[('Petron', 'Petron'), ('Shell', 'Shell')], max_length=100, null=True)),
                ('fleetcard_type', models.CharField(blank=True, choices=[('Single', 'Single'), ('Driver', 'Driver'), ('Vehicle', 'Vehicle')], max_length=100, null=True)),
                ('fuel_limit_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('fuel_limit_quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('products_restriction', models.CharField(blank=True, choices=[('S: Super Only', 'S: Super Only'), ('U: Super Unleaded Only', 'U: Super Unleaded Only'), ('R: Regular Only', 'R: Regular Only'), ('X: Velocity', 'X: Velocity'), ('D: Diesoline Only', 'D: Diesoline Only'), ('L: Lubricant Only', 'L: Lubricant Only'), ('V: Service Only', 'V: Service Only'), ('C: Convenience store items, sundries, accesories', 'C: Convenience store items, sundries, accesories')], max_length=100, null=True)),
                ('req_employee', models.CharField(blank=True, max_length=100, null=True)),
                ('req_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('req_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('req_title', models.CharField(blank=True, max_length=100, null=True)),
                ('req_cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('atd_no', models.CharField(blank=True, max_length=100, null=True)),
                ('temporary_atd', models.CharField(blank=True, max_length=100, null=True)),
                ('new_emp_id', models.CharField(blank=True, max_length=100, null=True)),
                ('new_emp_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('new_emp_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('new_emp_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('new_temp_atd', models.CharField(blank=True, max_length=100, null=True)),
                ('new_assignee', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_center_code', models.CharField(blank=True, max_length=100, null=True)),
                ('cancellation', models.CharField(blank=True, choices=[('Disposal Of Vehicle', 'Disposal Of Vehicle'), ('Resignation of User', 'Resignation of User')], max_length=100, null=True)),
                ('plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('con_sticker', models.CharField(blank=True, max_length=100, null=True)),
                ('model_year', models.CharField(blank=True, max_length=100, null=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('make', models.CharField(blank=True, max_length=100, null=True)),
                ('fuel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('new_plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('new_cond_sticker', models.CharField(blank=True, max_length=100, null=True)),
                ('new_model_year', models.CharField(blank=True, max_length=100, null=True)),
                ('new_vbrand', models.CharField(blank=True, max_length=100, null=True)),
                ('new_vmake', models.CharField(blank=True, max_length=100, null=True)),
                ('new_vfuel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('approved_by', models.CharField(blank=True, choices=[('Ser Roy Perluval Dela Cruz', 'Ser Roy Perluval Dela Cruz')], max_length=100, null=True)),
                ('date_summitted', models.CharField(blank=True, max_length=100, null=True)),
                ('fleet_received', models.CharField(blank=True, max_length=100, null=True)),
                ('fleet_card_no', models.CharField(blank=True, max_length=100, null=True)),
                ('fleet_date_release', models.CharField(blank=True, max_length=100, null=True)),
                ('person_release', models.CharField(blank=True, max_length=100, null=True)),
                ('date_initiated', models.DateField(blank=True, editable=False)),
                ('GCR_SLA', models.CharField(blank=True, max_length=20, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical gas_card',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Historicalservice_vehicle',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('request_date', models.CharField(blank=True, max_length=100, null=True)),
                ('req_employee_id', models.CharField(blank=True, max_length=100, null=True)),
                ('req_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('req_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_employee_id', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_group', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_costcenter', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_section', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_location', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_atd', models.CharField(blank=True, max_length=100, null=True)),
                ('new_employee_id', models.CharField(blank=True, max_length=100, null=True)),
                ('new_employee_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('new_employee_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('new_employee_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('new_temporary_atd', models.CharField(blank=True, max_length=100, null=True)),
                ('prefered_vehicle', models.CharField(blank=True, choices=[('Sedan', 'Sedan'), ('SUV', 'SUV '), ('Pick up 4x2', 'Pick up 4x2'), ('Pick Up 4x4', 'Pick Up 4x4')], max_length=100, null=True)),
                ('E_plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('E_con_sticker', models.CharField(blank=True, max_length=100, null=True)),
                ('E_model_year', models.CharField(blank=True, max_length=100, null=True)),
                ('E_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('E_make', models.CharField(blank=True, max_length=100, null=True)),
                ('E_type', models.CharField(blank=True, max_length=100, null=True)),
                ('approved_by', models.CharField(blank=True, choices=[('Ser Roy Dela Cruz', 'Ser Roy Dela Cruz'), ('Adolfo Carlos Umali', 'Adolfo Carlos Umali ')], max_length=100, null=True)),
                ('approved_date', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_provider', models.CharField(blank=True, choices=[('Orix', 'Orix'), ('Diamond', 'Diamond '), ('Safari', 'Safari')], max_length=100, null=True)),
                ('vehicle_plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_CS_no', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_brand', models.CharField(blank=True, choices=[('BMW', 'BMW'), ('Chevrolet', 'Chevrolet '), ('chrysler', 'chrysler'), ('Ford', 'Ford'), ('Honda', 'Honda '), ('Hyundai', 'Hyundai'), ('Isuzu', 'Isuzu'), ('Kia', 'Kia '), ('Masda', 'Masda'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan '), ('Peugeot', 'Peugeot'), ('Subaro', 'Subaro')], max_length=100, null=True)),
                ('vehicle_make', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_fuel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('SVV_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('date_initiated', models.DateField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical service_vehicle',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalVehicle_Repair',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('request_date', models.DateField(null=True)),
                ('employee', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('group_section', models.CharField(blank=True, max_length=100, null=True)),
                ('plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('v_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('engine', models.CharField(blank=True, max_length=100, null=True)),
                ('v_make', models.CharField(blank=True, max_length=100, null=True)),
                ('v_model', models.CharField(blank=True, max_length=100, null=True)),
                ('chassis', models.CharField(blank=True, max_length=100, null=True)),
                ('band', models.CharField(blank=True, max_length=100, null=True)),
                ('cond_sticker', models.CharField(blank=True, max_length=100, null=True)),
                ('equipment_no', models.CharField(blank=True, max_length=100, null=True)),
                ('fleet_area', models.CharField(blank=True, choices=[('The Globe Tower', 'The Globe Tower'), ('Visayas-Mindanao', 'Visayas-Mindanao')], max_length=100, null=True)),
                ('particulars', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('maintenance_type1', models.CharField(blank=True, choices=[('Preventive Maintenance', 'Preventive Maintenance'), ('Corective Maitenance', 'Corective Maitenance'), ('Battery', 'Battery'), ('Tire', 'Tire')], max_length=100, null=True)),
                ('scope_work1', models.CharField(blank=True, max_length=100, null=True)),
                ('maintenance_type2', models.CharField(blank=True, choices=[('Preventive Maintenance', 'Preventive Maintenance'), ('Corective Maitenance', 'Corective Maitenance'), ('Battery', 'Battery'), ('Tire', 'Tire')], max_length=100, null=True)),
                ('scope_work2', models.CharField(blank=True, max_length=100, null=True)),
                ('recommendations', models.CharField(blank=True, max_length=100, null=True)),
                ('service_reminder', models.CharField(blank=True, max_length=100, null=True)),
                ('verified_by', models.CharField(blank=True, choices=[('Shane Santos', 'Shane Santos')], max_length=100, null=True)),
                ('work_order1', models.CharField(blank=True, max_length=100, null=True)),
                ('work_order2', models.CharField(blank=True, max_length=100, null=True)),
                ('work_order3', models.CharField(blank=True, max_length=100, null=True)),
                ('datework_created', models.CharField(blank=True, max_length=100, null=True)),
                ('Shop_vendor', models.CharField(blank=True, choices=[('GR8', 'GR8'), ('Others', 'Others')], max_length=100, null=True)),
                ('date_forwarded', models.CharField(blank=True, max_length=100, null=True)),
                ('estimate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('maintenance_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('less_discount', models.CharField(blank=True, max_length=100, null=True)),
                ('estimate_remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('estimate_attached', models.CharField(blank=True, max_length=100, null=True)),
                ('approvedby', models.CharField(blank=True, choices=[('Ser Roy Perluval Dela Cruz', 'Ser Roy Perluval Dela Cruz'), ('Adolfo Carlos Umali', 'Adolfo Carlos Umali')], max_length=100, null=True)),
                ('meter_reading', models.CharField(blank=True, max_length=100, null=True)),
                ('VRR_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('date_initiated', models.DateField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical vehicle_ repair',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='service_vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('request_date', models.CharField(blank=True, max_length=100, null=True)),
                ('req_employee_id', models.CharField(blank=True, max_length=100, null=True)),
                ('req_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('req_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_employee_id', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_group', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_costcenter', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_section', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_location', models.CharField(blank=True, max_length=100, null=True)),
                ('assignee_atd', models.CharField(blank=True, max_length=100, null=True)),
                ('new_employee_id', models.CharField(blank=True, max_length=100, null=True)),
                ('new_employee_fname', models.CharField(blank=True, max_length=100, null=True)),
                ('new_employee_lname', models.CharField(blank=True, max_length=100, null=True)),
                ('new_employee_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('new_temporary_atd', models.CharField(blank=True, max_length=100, null=True)),
                ('prefered_vehicle', models.CharField(blank=True, choices=[('Sedan', 'Sedan'), ('SUV', 'SUV '), ('Pick up 4x2', 'Pick up 4x2'), ('Pick Up 4x4', 'Pick Up 4x4')], max_length=100, null=True)),
                ('E_plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('E_con_sticker', models.CharField(blank=True, max_length=100, null=True)),
                ('E_model_year', models.CharField(blank=True, max_length=100, null=True)),
                ('E_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('E_make', models.CharField(blank=True, max_length=100, null=True)),
                ('E_type', models.CharField(blank=True, max_length=100, null=True)),
                ('approved_by', models.CharField(blank=True, choices=[('Ser Roy Dela Cruz', 'Ser Roy Dela Cruz'), ('Adolfo Carlos Umali', 'Adolfo Carlos Umali ')], max_length=100, null=True)),
                ('approved_date', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_provider', models.CharField(blank=True, choices=[('Orix', 'Orix'), ('Diamond', 'Diamond '), ('Safari', 'Safari')], max_length=100, null=True)),
                ('vehicle_plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_CS_no', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_brand', models.CharField(blank=True, choices=[('BMW', 'BMW'), ('Chevrolet', 'Chevrolet '), ('chrysler', 'chrysler'), ('Ford', 'Ford'), ('Honda', 'Honda '), ('Hyundai', 'Hyundai'), ('Isuzu', 'Isuzu'), ('Kia', 'Kia '), ('Masda', 'Masda'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan '), ('Peugeot', 'Peugeot'), ('Subaro', 'Subaro')], max_length=100, null=True)),
                ('vehicle_make', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_fuel_type', models.CharField(blank=True, max_length=100, null=True)),
                ('SVV_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('date_initiated', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('request_date', models.DateField(null=True)),
                ('employee', models.CharField(blank=True, max_length=100, null=True)),
                ('cost_center', models.CharField(blank=True, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('group_section', models.CharField(blank=True, max_length=100, null=True)),
                ('plate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('v_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('engine', models.CharField(blank=True, max_length=100, null=True)),
                ('v_make', models.CharField(blank=True, max_length=100, null=True)),
                ('v_model', models.CharField(blank=True, max_length=100, null=True)),
                ('chassis', models.CharField(blank=True, max_length=100, null=True)),
                ('band', models.CharField(blank=True, max_length=100, null=True)),
                ('cond_sticker', models.CharField(blank=True, max_length=100, null=True)),
                ('equipment_no', models.CharField(blank=True, max_length=100, null=True)),
                ('fleet_area', models.CharField(blank=True, choices=[('The Globe Tower', 'The Globe Tower'), ('Visayas-Mindanao', 'Visayas-Mindanao')], max_length=100, null=True)),
                ('particulars', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('maintenance_type1', models.CharField(blank=True, choices=[('Preventive Maintenance', 'Preventive Maintenance'), ('Corective Maitenance', 'Corective Maitenance'), ('Battery', 'Battery'), ('Tire', 'Tire')], max_length=100, null=True)),
                ('scope_work1', models.CharField(blank=True, max_length=100, null=True)),
                ('maintenance_type2', models.CharField(blank=True, choices=[('Preventive Maintenance', 'Preventive Maintenance'), ('Corective Maitenance', 'Corective Maitenance'), ('Battery', 'Battery'), ('Tire', 'Tire')], max_length=100, null=True)),
                ('scope_work2', models.CharField(blank=True, max_length=100, null=True)),
                ('recommendations', models.CharField(blank=True, max_length=100, null=True)),
                ('service_reminder', models.CharField(blank=True, max_length=100, null=True)),
                ('verified_by', models.CharField(blank=True, choices=[('Shane Santos', 'Shane Santos')], max_length=100, null=True)),
                ('work_order1', models.CharField(blank=True, max_length=100, null=True)),
                ('work_order2', models.CharField(blank=True, max_length=100, null=True)),
                ('work_order3', models.CharField(blank=True, max_length=100, null=True)),
                ('datework_created', models.CharField(blank=True, max_length=100, null=True)),
                ('Shop_vendor', models.CharField(blank=True, choices=[('GR8', 'GR8'), ('Others', 'Others')], max_length=100, null=True)),
                ('date_forwarded', models.CharField(blank=True, max_length=100, null=True)),
                ('estimate_no', models.CharField(blank=True, max_length=100, null=True)),
                ('maintenance_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('less_discount', models.CharField(blank=True, max_length=100, null=True)),
                ('estimate_remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('estimate_attached', models.CharField(blank=True, max_length=100, null=True)),
                ('approvedby', models.CharField(blank=True, choices=[('Ser Roy Perluval Dela Cruz', 'Ser Roy Perluval Dela Cruz'), ('Adolfo Carlos Umali', 'Adolfo Carlos Umali')], max_length=100, null=True)),
                ('meter_reading', models.CharField(blank=True, max_length=100, null=True)),
                ('VRR_SLA', models.CharField(blank=True, max_length=10, null=True)),
                ('date_initiated', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]
