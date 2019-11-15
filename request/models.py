from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
from masterlist.models import EmployeeMasterlist,VehicleMasterList

def increment_Activity_id():
	last_in = CarRentalRequest.objects.all().order_by('id').last()
	if not last_in:
	    return 'CRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'CRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id


class CarRentalRequest(models.Model):

	CHOICES= (
		('Ser Roy DelaCruz', 'Ser Roy DelaCruz'),
		('Adolfo Carlos Umali', 'Adolfo Carlos Umali'),
		)
	Rental= (
		('Daily', 'Daily'),
		('Monthly', 'Monthly'),
		)
	Vtype= (
		('Sedan', 'Sedan'),
		('SUV', 'SUV'),
		('VAN', 'VAN'),
	)

	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	A_Employee_Id = models.ForeignKey('masterlist.EmployeeMasterlist', on_delete=models.CASCADE)
	Date_received = models.DateField(auto_now=False, null=True)
	Assignee_Fname = models.CharField(max_length=100, null=True)
	Assignee_Lname = models.CharField(max_length=100, null=True)
	Assignee_No = models.CharField(max_length=50, null=True)
	Assignee_Company = models.CharField(max_length=200, null=True)
	Assignee_band = models.CharField(max_length=100,null=True)
	Assignee_Dept =models.CharField(max_length=100, null=True)
	Assignee_Cost = models.FloatField(null=True)
	Assignee_Div = models.CharField(max_length=100, null=True)
	Assignee_Loc = models.CharField(max_length=200, null=True)
	Assignee_Section = models.CharField(max_length=100, null=True)
	Assignee_Designation = models.CharField(max_length=100, null=True)
	Assignee_ATD = models.CharField(max_length=100, null=True)
	Vendor_name = models.CharField(max_length=100, null=True)
	Date = models.DateField(auto_now=False, null=True)
	Up_to = models.CharField(max_length=100, null=True)
	Time = models.TimeField(auto_now=False, auto_now_add=False, null=True)
	Place_of_del = models.CharField(max_length=100, null=True)
	type_rental = models.CharField(max_length=50, null=True, choices=Rental)
	Cost_center = models.FloatField(null=True)
	Rental_period = models.FloatField(null=True)
	Destination = models.CharField(max_length=100, null=True)
	Delivery_date = models.DateField(auto_now=False, null=True)
	End_user = models.CharField(max_length=100, null=True)
	Type_of_vehicle = models.CharField(max_length=50, null=True, choices=Vtype)
	Plate_no = models.CharField(max_length=50, null=True)
	Immediate_supervisor = models.CharField(max_length=50, null=True, choices=CHOICES)
	CR_SLA = models.CharField(max_length=10, null=True)
	Date_initiated = models.DateField(auto_now=True)


	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('carrequest_list')

def increment_Activity_id():
	last_in = Gas_card.objects.all().order_by('id').last()
	if not last_in:
		return 'GCR' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'GCR' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

class Gas_card(models.Model):
	card_type= (
	('Single', 'Single'),
	('Driver','Driver'),
	('Vehicle','Vehicle'),
	)
	fleet_card= (
	('Petron', 'Petron'),
	('Shell','Shell'),
	)
	app_type= (
	('Daily', 'Daily'),
	('Transfer Acountability', 'Transfer Acountability'),
	('Cancel - Disposal of Vehicle', 'Cancel - Disposal of Vehicle'),
	('Cancel - Resignation of User', 'Cancel - Resignation of User'),
	('Replacement - Damage', 'Replacement - Damage'),
	('Replacement - Lose', 'Replacement - Lose'),
	('Others - Adjust Credit Limit', 'Others - Adjust Credit Limit'),
	('Others - Change of Product Restriction', 'Others - Change of Product Restriction'),
	('Others - Update Cost Center', 'Others - Update Cost Center'),
	)
	restrictions= (
	('S: Super Only', 'S: Super Only'),
	('U: Super Unleaded Only', 'U: Super Unleaded Only'),
	('R: Regular Only', 'R: Regular Only'),
	('X: Velocity', 'X: Velocity'),
	('D: Diesoline Only', 'D: Diesoline Only'),
	('L: Lubricant Only', 'L: Lubricant Only'),
	('V: Service Only', 'V: Service Only'),
	('C: Convenience store items, sundries, accesories', 'C: Convenience store items, sundries, accesories'),
	)
	approved= (
		('Ser Roy Perluval Dela Cruz','Ser Roy Perluval Dela Cruz'),
	)
	cancellation= (
		('Disposal Of Vehicle','Disposal Of Vehicle'),
		('Resignation of User','Resignation of User'),
	)

	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	date_received = models.DateField(auto_now=False, null=True)
	application_type = models.CharField(max_length=100, null=True, choices=app_type)
	fleet_provider= models.CharField(max_length=100, null=True, choices=fleet_card)
	fleetcard_type = models.CharField(max_length=100, null=True, choices=card_type)
	fuel_limit_amount = models.CharField(max_length=100, null=True)
	fuel_limit_quantity = models.CharField(max_length=100, null=True)
	products_restriction = models.CharField(max_length=100, null=True, choices=restrictions)
	req_employee_id = models.ForeignKey('masterlist.EmployeeMasterlist', on_delete=models.CASCADE)
	req_fname = models.CharField(max_length=100, null=True)
	req_lname = models.CharField(max_length=100, null=True)
	req_title = models.CharField(max_length=100, null=True)
	req_cost_center = models.CharField(max_length=100, null=True)
	atd_no = models.CharField(max_length=100, null=True)
	temporary_atd = models.CharField(max_length=100, null=True)
	new_emp_id = models.CharField(max_length=100, null=True)
	new_emp_fname = models.CharField(max_length=100, null=True)
	new_emp_lname = models.CharField(max_length=100, null=True)
	new_emp_cost = models.CharField(max_length=100, null=True)
	new_temp_atd = models.CharField(max_length=100, null=True)
	new_assignee = models.CharField(max_length=100, null=True)
	cost_center_code = models.CharField(max_length=100, null=True)
	cancellation = models.CharField(max_length=100, null=True, choices=cancellation)
	plate_no = models.ForeignKey('masterlist.VehicleMasterList', on_delete=models.CASCADE)
	con_sticker = models.CharField(max_length=100, null=True)
	model_year = models.CharField(max_length=100, null=True)
	brand = models.CharField(max_length=100, null=True)
	make = models.CharField(max_length=100, null=True)
	fuel_type = models.CharField(max_length=100, null=True)
	new_plate_no = models.CharField(max_length=100, null=True)
	new_cond_sticker = models.CharField(max_length=100, null=True)
	new_model_year = models.CharField(max_length=100, null=True)
	new_vbrand = models.CharField(max_length=100, null=True)
	new_vmake = models.CharField(max_length=100, null=True)
	new_vfuel_type = models.CharField(max_length=100, null=True)
	approved_by = models.CharField(max_length=100, null=True, choices=approved)
	date_summitted =models.DateField(auto_now=False, null=True)
	fleet_received = models.DateField(auto_now=False, null=True)
	fleet_card_no = models.CharField(max_length=100, null=True)
	fleet_date_release = models.DateField(auto_now=False, null=True)
	person_release = models.CharField(max_length=100, null=True)
	date_initiated = models.DateField(auto_now=True)
	GCR_SLA = models.CharField(max_length=20, null=True)

	def __str__(self):
    		return self.Activity_id

	def get_absolute_url(self):
		return reverse('gascard_list')

def increment_Activity_id():
	last_in = service_vehicle.objects.all().order_by('id').last()
	if not last_in:
		return 'SVV' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'SVV' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id		

class service_vehicle(models.Model):
	vtype= (
		('Sedan', 'Sedan'),
		('SUV', 'SUV '),
		('Pick up 4x2', 'Pick up 4x2'),
		('Pick Up 4x4', 'Pick Up 4x4'),
		)
	approvedby= (
		('Ser Roy Dela Cruz', 'Ser Roy Dela Cruz'),
		('Adolfo Carlos Umali', 'Adolfo Carlos Umali '),
		)
	vprovider= (
		('Orix', 'Orix'),
		('Diamond', 'Diamond '),
		('Safari', 'Safari'),
		)
	vbrand= (
		('BMW', 'BMW'),
		('Chevrolet', 'Chevrolet '),
		('chrysler', 'chrysler'),
		('Ford', 'Ford'),
		('Honda', 'Honda '),
		('Hyundai', 'Hyundai'),
		('Isuzu', 'Isuzu'),
		('Kia', 'Kia '),
		('Masda', 'Masda'),
		('Mitsubishi', 'Mitsubishi'),
		('Nissan', 'Nissan '),
		('Peugeot', 'Peugeot'),
		('Subaro', 'Subaro'),
		)
	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	request_date = models.DateField(auto_now=False, null=True)
	req_employee_id = models.ForeignKey('masterlist.EmployeeMasterlist', on_delete=models.DO_NOTHING, related_name='req_employee_id')
	req_lname = models.CharField(max_length=100, null=True)
	req_fname = models.CharField(max_length=100, null=True)
	assignee_employee_id = models.ForeignKey('masterlist.EmployeeMasterlist', on_delete=models.DO_NOTHING,related_name='assignee_employee_id')
	assignee_group = models.CharField(max_length=100, null=True)
	assignee_fname = models.CharField(max_length=100, null=True)
	assignee_lname = models.CharField(max_length=100, null=True)
	assignee_costcenter = models.CharField(max_length=100, null=True)
	assignee_section = models.CharField(max_length=100, null=True)
	assignee_location = models.CharField(max_length=100, null=True)
	assignee_atd = models.CharField(max_length=100, null=True)
	new_employee_id = models.CharField(max_length=100, null=True)
	new_employee_fname = models.CharField(max_length=100, null=True)
	new_employee_lname = models.CharField(max_length=100, null=True)
	new_employee_cost = models.CharField(max_length=100, null=True)
	new_temporary_atd = models.CharField(max_length=100, null=True)
	prefered_vehicle = models.CharField(max_length=100, null=True, choices=vtype)
	E_plate_no = models.ForeignKey('masterlist.VehicleMasterList', on_delete=models.DO_NOTHING)
	E_con_sticker = models.CharField(max_length=100, null=True)
	E_model_year = models.CharField(max_length=100, null=True)
	E_brand = models.CharField(max_length=100, null=True)
	E_make = models.CharField(max_length=100, null=True)
	E_type = models.CharField(max_length=100, null=True)
	approved_by = models.CharField(max_length=100, null=True, choices=approvedby)
	approved_date = models.DateField(auto_now=False, null=True)
	vehicle_provider = models.CharField(max_length=100, null=True, choices=vprovider)
	vehicle_plate_no = models.CharField(max_length=100, null=True)
	vehicle_CS_no = models.CharField(max_length=100, null=True)
	vehicle_model = models.CharField(max_length=100, null=True)
	vehicle_brand = models.CharField(max_length=100, null=True, choices=vbrand)
	vehicle_make = models.CharField(max_length=100, null=True)
	vehicle_fuel_type = models.CharField(max_length=100, null=True)
	SVV_SLA = models.CharField(max_length=10, null=True)
	date_initiated = models.DateField(auto_now=True, null=True)

	def __str__(self):
    		return self.Activity_id

	def get_absolute_url(self):
		return reverse('service_list')


def increment_Activity_id():
	last_in = Vehicle_Repair.objects.all().order_by('id').last()
	if not last_in:
		return 'VRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'VRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

class Vehicle_Repair(models.Model):
	area= (
	('The Globe Tower', 'The Globe Tower'),
	('Visayas-Mindanao', 'Visayas-Mindanao '),
	)
	
	verified= (
		('Shane Santos','Shane Santos'),
	)
	shop= (
		('GR8','GR8'),
		('Rapide','Rapide'),
		('EV','EV')
	)
	maintenance= (
		('Preventive Maintenance','Preventive Maintenance'),
		('Corective Maitenance','Corective Maitenance'),
		('Battery','Battery'),
		('Tire','Tire'),
	)
	approvedby= (
		('Ser Roy Perluval Dela Cruz','Ser Roy Perluval Dela Cruz'),
		('Adolfo Carlos Umali','Adolfo Carlos Umali'),
	)
	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	request_date = models.DateField(auto_now=False, null=True)
	employee_Id = models.ForeignKey('masterlist.EmployeeMasterlist', on_delete=models.DO_NOTHING)
	cost_center = models.CharField(max_length=100, null=True)
	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=True)
	contact_no = models.CharField(max_length=100, null=True)
	company = models.CharField(max_length=100, null=True)
	department = models.CharField(max_length=100, null=True)
	group_section = models.CharField(max_length=100, null=True)
	plate_no = models.ForeignKey('masterlist.VehicleMasterList', on_delete=models.DO_NOTHING)
	v_brand = models.CharField(max_length=100, null=True)
	engine = models.CharField(max_length=100, null=True)
	v_make = models.CharField(max_length=100, null=True)
	v_model = models.CharField(max_length=100, null=True)
	chassis = models.CharField(max_length=100, null=True)
	band = models.CharField(max_length=100, null=True)
	cond_sticker = models.CharField(max_length=100, null=True)
	equipment_no = models.CharField(max_length=100, null=True)
	fleet_area = models.CharField(max_length=100, null=True, choices=area)
	particulars = models.CharField(max_length=100, null=True)
	category = models.CharField(max_length=100, null=True)
	maintenance_type1 = models.CharField(max_length=100, null=True, choices=maintenance)
	scope_work1 = models.CharField(max_length=100, null=True)
	maintenance_type2 = models.CharField(max_length=100, null=True, choices=maintenance)
	scope_work2 = models.CharField(max_length=100, null=True)
	recommendations = models.CharField(max_length=100, null=True)
	service_reminder = models.CharField(max_length=100, null=True)
	verified_by = models.CharField(max_length=100, null=True, choices=verified)
	work_order1 = models.CharField(max_length=100, null=True)
	work_order2 = models.CharField(max_length=100, null=True)
	work_order3 = models.CharField(max_length=100, null=True)
	datework_created = models.DateField(auto_now=False, null=True)
	Shop_vendor = models.CharField(max_length=100, null=True, choices=shop)
	date_forwarded = models.CharField(max_length=100, null=True)
	estimate_no = models.CharField(max_length=100, null=True)
	maintenance_amount = models.CharField(max_length=100, null=True)
	less_discount = models.CharField(max_length=100, null=True)
	estimate_remarks = models.CharField(max_length=100, null=True)
	estimate_attached = models.CharField(max_length=100, null=True)
	approvedby = models.CharField(max_length=100, null=True, choices=approvedby)
	meter_reading = models.CharField(max_length=100, null=True)
	VRR_SLA = models.CharField(max_length=10, null=True)
	date_initiated = models.DateField(auto_now=True, null=True)

	def __str__(self):
    		return self.Activity_id

	def get_absolute_url(self):
		return reverse('repair_list')


