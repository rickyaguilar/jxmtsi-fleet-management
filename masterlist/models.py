from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
from django.contrib.auth.models import User




class EmployeeMasterlist(models.Model):
	Company = models.CharField(max_length=100, null=True)
	# Employee_Id = models.ForeignKey('payment.Employee_Id', on_delete=models.SET_DEFAULT, related_name='Employee_id')
	Employee_Id = models.CharField(max_length=100, null=True)
	Last_name = models.CharField(max_length=50, null=True)
	First_name = models.CharField(max_length=50, null=True)
	Middle_name = models.CharField(max_length=5, null=True)
	Suffix = models.CharField(max_length=20, null=True)
	External_role = models.CharField(max_length=100, null=True)
	Job_category = models.CharField(max_length=100, null=True)
	Hiring_date = models.DateField(auto_now=False, null=True)
	Tenure = models.FloatField(null=True)
	Band = models.CharField(max_length=50, null=True)
	Cost_center = models.CharField(max_length=100, null=True)
	DIV_code = models.CharField(max_length=100, null=True)
	Group = models.CharField(max_length=100, null=True)
	Division = models.CharField(max_length=100, null=True)
	Department = models.CharField(max_length=100, null=True)
	Section = models.CharField(max_length=100, null=True)
	Unit = models.CharField(max_length=100, null=True)
	Sub_unit = models.CharField(max_length=100, null=True)
	IS_ID = models.CharField(max_length=100, null=True)
	IS_lastname = models.CharField(max_length=100, null=True)
	IS_firstname = models.CharField(max_length=100, null=True)
	Location = models.CharField(max_length=100, null=True)
	Area = models.CharField(max_length=100, null=True)
	Area2 = models.CharField(max_length=100, null=True)
	Benefit = models.CharField(max_length=100, null=True)

	def get_absolute_url(self):
		return reverse('employee-list')

def increment_Activity_id():
	last_in = VehicleMasterList.objects.all().order_by('id').last()
	if not last_in:
	    return 'VML' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'VML' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

def increment_No():
	last_in = VehicleMasterList.objects.all().order_by('id').last()
	if not last_in:
	    return '1'
	in_id = last_in.No
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = str(new_in_int).zfill(1)
	return new_in_id

class VehicleMasterList(models.Model):

	# Vbrand= (
	#       ('Honda','Honda'),
	#       ('Toyota','Toyota'),
	#       ('Mitsubishi','Mitsubishi'),
	#       ('Ford','Ford'),
	#       ('Masda','Masda'),
	#       ('Isuzu','Isuzu'),
	#       ('Hyundai','Hyundai'),
	#       ('Nissan','Nissan'),
	#       ('SuZuki','Suzuki'),
	#       ('Chevrolet','Chevrolet'),
	# )

	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	No = models.CharField(max_length=50, null=True, default=increment_No)
	Plate_no = models.CharField(max_length=50, null=True)
	Conduction_Sticker = models.CharField(max_length=100, null=True)
	Remarks = models.CharField(max_length=100, null=True)
	CR_name = models.CharField(max_length=100, null=True)
	Ending = models.CharField(max_length=20, null=True)
	Model = models.CharField(max_length=50, null=True)
	Brand = models.CharField(max_length=50, null=True)
	Vehicle_make = models.CharField(max_length=100, null=True)
	Engine_No = models.CharField(max_length=100, null=True)
	Chassis_no = models.CharField(max_length=100, null=True)
	MV_file_no = models.CharField(max_length=100, null=True)
	vehicle_type = models.CharField(max_length=100, null=True)
	Vehicle_category = models.CharField(max_length=100, null=True)
	Employee_Id = models.CharField(max_length=50, null=True)
	Band_level = models.CharField(max_length=50, null=True)
	Band_Benefit = models.CharField(max_length=50, null=True)
	Contact_no = models.CharField(max_length=50, null=True)
	Cost_center = models.CharField(max_length=100,null=True)
	Group =models.CharField(max_length=100, null=True)
	Division = models.CharField(max_length=100, null=True)
	Department = models.CharField(max_length=100, null=True)
	Section = models.CharField(max_length=100, null=True)
	IS_employee_ID = models.CharField(max_length=100, null=True)
	IS_firstname = models.CharField(max_length=100, null=True)
	IS_lastname = models.CharField(max_length=100, null=True)
	Location = models.CharField(max_length=100, null=True)
	Aquisition_date = models.DateField(auto_now=False, null=True)
	Aquisition_cost = models.CharField(max_length=100, null=True)
	Asset_no = models.CharField(max_length=100, null=True)
	PO_no = models.CharField(max_length=100, null=True)
	SAP_PR = models.CharField(max_length=100, null=True)
	Vehicle_IVN_no = models.CharField(max_length=100, null=True)
	Unit_MATDOC = models.CharField(max_length=100, null=True)
	Grdd_date = models.CharField(max_length=100, null=True)
	Equipment_no = models.CharField(max_length=100, null=True)
	Latest_registration = models.DateField(auto_now=False, null=True)
	Lates_remark = models.CharField(max_length=100, null=True)
	Lname_assignee = models.CharField(max_length=50, null=True)
	Fname_assignee = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('vehicle-list')







