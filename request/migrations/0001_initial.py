# Generated by Django 2.1.7 on 2019-11-05 02:02

from django.db import migrations, models
import django.db.models.deletion
import request.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masterlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarRentalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('Date_received', models.DateField(null=True)),
                ('Assignee_Fname', models.CharField(max_length=100, null=True)),
                ('Assignee_Lname', models.CharField(max_length=100, null=True)),
                ('Assignee_No', models.CharField(max_length=50, null=True)),
                ('Assignee_Company', models.CharField(max_length=200, null=True)),
                ('Assignee_band', models.CharField(max_length=100, null=True)),
                ('Assignee_Dept', models.CharField(max_length=100, null=True)),
                ('Assignee_Cost', models.FloatField(null=True)),
                ('Assignee_Div', models.CharField(max_length=100, null=True)),
                ('Assignee_Loc', models.CharField(max_length=200, null=True)),
                ('Assignee_Section', models.CharField(max_length=100, null=True)),
                ('Assignee_Designation', models.CharField(max_length=100, null=True)),
                ('Assignee_ATD', models.CharField(max_length=100, null=True)),
                ('Vendor_name', models.CharField(max_length=100, null=True)),
                ('Date', models.DateField(null=True)),
                ('Up_to', models.CharField(max_length=100, null=True)),
                ('Time', models.TimeField(null=True)),
                ('Place_of_del', models.CharField(max_length=100, null=True)),
                ('type_rental', models.CharField(choices=[('Daily', 'Daily'), ('Monthly', 'Monthly')], max_length=50, null=True)),
                ('Cost_center', models.FloatField(null=True)),
                ('Rental_period', models.FloatField(null=True)),
                ('Destination', models.CharField(max_length=100, null=True)),
                ('Delivery_date', models.DateField(null=True)),
                ('End_user', models.CharField(max_length=100, null=True)),
                ('Type_of_vehicle', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('VAN', 'VAN')], max_length=50, null=True)),
                ('Plate_no', models.CharField(max_length=50, null=True)),
                ('Immediate_supervisor', models.CharField(choices=[('Ser Roy DelaCruz', 'Ser Roy DelaCruz'), ('Adolfo Carlos Umali', 'Adolfo Carlos Umali')], max_length=50, null=True)),
                ('CR_SLA', models.CharField(max_length=10, null=True)),
                ('Date_initiated', models.DateField(auto_now=True)),
                ('A_Employee_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterlist.EmployeeMasterlist')),
            ],
        ),
        migrations.CreateModel(
            name='Gas_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('date_received', models.DateField(null=True)),
                ('application_type', models.CharField(choices=[('Daily', 'Daily'), ('Transfer Acountability', 'Transfer Acountability'), ('Cancel - Disposal of Vehicle', 'Cancel - Disposal of Vehicle'), ('Cancel - Resignation of User', 'Cancel - Resignation of User'), ('Replacement - Damage', 'Replacement - Damage'), ('Replacement - Lose', 'Replacement - Lose'), ('Others - Adjust Credit Limit', 'Others - Adjust Credit Limit'), ('Others - Change of Product Restriction', 'Others - Change of Product Restriction'), ('Others - Update Cost Center', 'Others - Update Cost Center')], max_length=100, null=True)),
                ('fleet_provider', models.CharField(choices=[('Petron', 'Petron'), ('Shell', 'Shell')], max_length=100, null=True)),
                ('fleetcard_type', models.CharField(choices=[('Single', 'Single'), ('Driver', 'Driver'), ('Vehicle', 'Vehicle')], max_length=100, null=True)),
                ('fuel_limit_amount', models.CharField(max_length=100, null=True)),
                ('fuel_limit_quantity', models.CharField(max_length=100, null=True)),
                ('products_restriction', models.CharField(choices=[('S: Super Only', 'S: Super Only'), ('U: Super Unleaded Only', 'U: Super Unleaded Only'), ('R: Regular Only', 'R: Regular Only'), ('X: Velocity', 'X: Velocity'), ('D: Diesoline Only', 'D: Diesoline Only'), ('L: Lubricant Only', 'L: Lubricant Only'), ('V: Service Only', 'V: Service Only'), ('C: Convenience store items, sundries, accesories', 'C: Convenience store items, sundries, accesories')], max_length=100, null=True)),
                ('req_employee_id', models.CharField(max_length=100, null=True)),
                ('req_fname', models.CharField(max_length=100, null=True)),
                ('req_lname', models.CharField(max_length=100, null=True)),
                ('req_title', models.CharField(max_length=100, null=True)),
                ('req_cost_center', models.CharField(max_length=100, null=True)),
                ('atd_no', models.CharField(max_length=100, null=True)),
                ('temporary_atd', models.CharField(max_length=100, null=True)),
                ('new_emp_id', models.CharField(max_length=100, null=True)),
                ('new_emp_fname', models.CharField(max_length=100, null=True)),
                ('new_emp_lname', models.CharField(max_length=100, null=True)),
                ('new_emp_cost', models.CharField(max_length=100, null=True)),
                ('new_temp_atd', models.CharField(max_length=100, null=True)),
                ('new_assignee', models.CharField(max_length=100, null=True)),
                ('cost_center_code', models.CharField(max_length=100, null=True)),
                ('cancellation', models.CharField(choices=[('Disposal Of Vehicle', 'Disposal Of Vehicle'), ('Resignation of User', 'Resignation of User')], max_length=100, null=True)),
                ('plate_no', models.CharField(max_length=100, null=True)),
                ('con_sticker', models.CharField(max_length=100, null=True)),
                ('model_year', models.CharField(max_length=100, null=True)),
                ('brand', models.CharField(max_length=100, null=True)),
                ('make', models.CharField(max_length=100, null=True)),
                ('fuel_type', models.CharField(max_length=100, null=True)),
                ('new_plate_no', models.CharField(max_length=100, null=True)),
                ('new_cond_sticker', models.CharField(max_length=100, null=True)),
                ('new_model_year', models.CharField(max_length=100, null=True)),
                ('new_vbrand', models.CharField(max_length=100, null=True)),
                ('new_vmake', models.CharField(max_length=100, null=True)),
                ('new_vfuel_type', models.CharField(max_length=100, null=True)),
                ('approved_by', models.CharField(choices=[('Ser Roy Perluval Dela Cruz', 'Ser Roy Perluval Dela Cruz')], max_length=100, null=True)),
                ('date_summitted', models.DateField(null=True)),
                ('fleet_received', models.DateField(null=True)),
                ('fleet_card_no', models.CharField(max_length=100, null=True)),
                ('fleet_date_release', models.DateField(null=True)),
                ('person_release', models.CharField(max_length=100, null=True)),
                ('date_initiated', models.DateField(auto_now=True)),
                ('GCR_SLA', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='service_vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('request_date', models.DateField(null=True)),
                ('req_lname', models.CharField(max_length=100, null=True)),
                ('req_fname', models.CharField(max_length=100, null=True)),
                ('assignee_group', models.CharField(max_length=100, null=True)),
                ('assignee_fname', models.CharField(max_length=100, null=True)),
                ('assignee_lname', models.CharField(max_length=100, null=True)),
                ('assignee_costcenter', models.CharField(max_length=100, null=True)),
                ('assignee_section', models.CharField(max_length=100, null=True)),
                ('assignee_location', models.CharField(max_length=100, null=True)),
                ('assignee_atd', models.CharField(max_length=100, null=True)),
                ('new_employee_id', models.CharField(max_length=100, null=True)),
                ('new_employee_fname', models.CharField(max_length=100, null=True)),
                ('new_employee_lname', models.CharField(max_length=100, null=True)),
                ('new_employee_cost', models.CharField(max_length=100, null=True)),
                ('new_temporary_atd', models.CharField(max_length=100, null=True)),
                ('prefered_vehicle', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV '), ('Pick up 4x2', 'Pick up 4x2'), ('Pick Up 4x4', 'Pick Up 4x4')], max_length=100, null=True)),
                ('E_plate_no', models.CharField(max_length=100, null=True)),
                ('E_con_sticker', models.CharField(max_length=100, null=True)),
                ('E_model_year', models.CharField(max_length=100, null=True)),
                ('E_brand', models.CharField(max_length=100, null=True)),
                ('E_make', models.CharField(max_length=100, null=True)),
                ('E_type', models.CharField(max_length=100, null=True)),
                ('approved_by', models.CharField(choices=[('Ser Roy Dela Cruz', 'Ser Roy Dela Cruz'), ('Adolfo Carlos Umali', 'Adolfo Carlos Umali ')], max_length=100, null=True)),
                ('approved_date', models.DateField(null=True)),
                ('vehicle_provider', models.CharField(choices=[('Orix', 'Orix'), ('Diamond', 'Diamond '), ('Safari', 'Safari')], max_length=100, null=True)),
                ('vehicle_plate_no', models.CharField(max_length=100, null=True)),
                ('vehicle_CS_no', models.CharField(max_length=100, null=True)),
                ('vehicle_model', models.CharField(max_length=100, null=True)),
                ('vehicle_brand', models.CharField(choices=[('BMW', 'BMW'), ('Chevrolet', 'Chevrolet '), ('chrysler', 'chrysler'), ('Ford', 'Ford'), ('Honda', 'Honda '), ('Hyundai', 'Hyundai'), ('Isuzu', 'Isuzu'), ('Kia', 'Kia '), ('Masda', 'Masda'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan '), ('Peugeot', 'Peugeot'), ('Subaro', 'Subaro')], max_length=100, null=True)),
                ('vehicle_make', models.CharField(max_length=100, null=True)),
                ('vehicle_fuel_type', models.CharField(max_length=100, null=True)),
                ('SVV_SLA', models.CharField(max_length=10, null=True)),
                ('date_initiated', models.DateField(auto_now=True, null=True)),
                ('assignee_employee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='assignee_employee_id', to='masterlist.EmployeeMasterlist')),
                ('req_employee_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='req_employee_id', to='masterlist.EmployeeMasterlist')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Activity_id', models.CharField(default=request.models.increment_Activity_id, max_length=100, null=True)),
                ('request_date', models.DateField(null=True)),
                ('cost_center', models.CharField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('contact_no', models.CharField(max_length=100, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('group_section', models.CharField(max_length=100, null=True)),
                ('v_brand', models.CharField(max_length=100, null=True)),
                ('engine', models.CharField(max_length=100, null=True)),
                ('v_make', models.CharField(max_length=100, null=True)),
                ('v_model', models.CharField(max_length=100, null=True)),
                ('chassis', models.CharField(max_length=100, null=True)),
                ('band', models.CharField(max_length=100, null=True)),
                ('cond_sticker', models.CharField(max_length=100, null=True)),
                ('equipment_no', models.CharField(max_length=100, null=True)),
                ('fleet_area', models.CharField(choices=[('The Globe Tower', 'The Globe Tower'), ('Visayas-Mindanao', 'Visayas-Mindanao ')], max_length=100, null=True)),
                ('particulars', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
                ('maintenance_type1', models.CharField(choices=[('Preventive Maintenance', 'Preventive Maintenance'), ('Corective Maitenance', 'Corective Maitenance'), ('Battery', 'Battery'), ('Tire', 'Tire')], max_length=100, null=True)),
                ('scope_work1', models.CharField(max_length=100, null=True)),
                ('maintenance_type2', models.CharField(choices=[('Preventive Maintenance', 'Preventive Maintenance'), ('Corective Maitenance', 'Corective Maitenance'), ('Battery', 'Battery'), ('Tire', 'Tire')], max_length=100, null=True)),
                ('scope_work2', models.CharField(max_length=100, null=True)),
                ('recommendations', models.CharField(max_length=100, null=True)),
                ('service_reminder', models.CharField(max_length=100, null=True)),
                ('verified_by', models.CharField(choices=[('Shane Santos', 'Shane Santos')], max_length=100, null=True)),
                ('work_order1', models.CharField(max_length=100, null=True)),
                ('work_order2', models.CharField(max_length=100, null=True)),
                ('work_order3', models.CharField(max_length=100, null=True)),
                ('datework_created', models.DateField(null=True)),
                ('Shop_vendor', models.CharField(choices=[('GR8', 'GR8'), ('Rapide', 'Rapide'), ('EV', 'EV')], max_length=100, null=True)),
                ('date_forwarded', models.CharField(max_length=100, null=True)),
                ('estimate_no', models.CharField(max_length=100, null=True)),
                ('maintenance_amount', models.CharField(max_length=100, null=True)),
                ('less_discount', models.CharField(max_length=100, null=True)),
                ('estimate_remarks', models.CharField(max_length=100, null=True)),
                ('estimate_attached', models.CharField(max_length=100, null=True)),
                ('approvedby', models.CharField(choices=[('Ser Roy Perluval Dela Cruz', 'Ser Roy Perluval Dela Cruz'), ('Adolfo Carlos Umali', 'Adolfo Carlos Umali')], max_length=100, null=True)),
                ('meter_reading', models.CharField(max_length=100, null=True)),
                ('VRR_SLA', models.CharField(max_length=10, null=True)),
                ('date_initiated', models.DateField(auto_now=True, null=True)),
                ('employee_Id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='masterlist.EmployeeMasterlist')),
                ('plate_no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='masterlist.VehicleMasterList')),
            ],
        ),
    ]