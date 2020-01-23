from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date

class EmployeeMasterlist(models.Model):
	Company = models.CharField(max_length=100, null=True)
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

	def __str__(self):
		return self.Employee_Id
		
	def get_absolute_url(self):
		return reverse('employee-list')

def increment_Activity_Id():
	last_in = VehicleMasterList.objects.all().order_by('id').last()
	if not last_in:
	    return 'VML' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000000'
	in_id = last_in.Activity_Id
	in_int = int(in_id[8:])
	new_in_int = in_int + 1
	new_in_id = 'VML' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

def increment_NO():
	last_in = VehicleMasterList.objects.all().order_by('id').last()
	if not last_in:
	    return '000000'
	in_id = last_in.NO
	in_int = int(in_id[0:])
	new_in_int = in_int + 1
	new_in_id = str(new_in_int).zfill(6)
	return new_in_id

class VehicleMasterList(models.Model):
	Vbrand= (
          ('Honda','Honda'),
          ('Toyota','Toyota'),
          ('Mitsubishi','Mitsubishi'),
          ('Ford','Ford'),
          ('Masda','Masda'),
          ('Isuzu','Isuzu'),
          ('Hyundai','Hyundai'),
          ('Nissan','Nissan'),
          ('SuZuki','Suzuki'),
          ('Chevrolet','Chevrolet'),
            )
	
	Activity_Id  = models.CharField(max_length=100,null=True, default=increment_Activity_Id)
	NO = models.CharField(max_length=100, null=True, default=increment_NO)
	PLATE_NO = models.CharField(max_length=100, null=True)
	CS_NO = models.CharField(max_length=100, null=True)
	CR_NAME = models.CharField(max_length=100, null=True)
	PLATE_ENDING = models.CharField(max_length=100, null=True)
	REGISTRATION_MONTH = models.CharField(max_length=100, null=True)
	MODEL = models.CharField(max_length=100, null=True)
	BRAND = models.CharField(max_length=100, null=True, choices=Vbrand)
	VEHICLE_MAKE = models.CharField(max_length=100, null=True)
	ENGINE_NO = models.CharField(max_length=100, null=True)
	CHASSIS_NO = models.CharField(max_length=100, null=True)
	MV_FILE_NO = models.CharField(max_length=100, null=True)
	VEHICLE_TYPE = models.CharField(max_length=100, null=True)
	ASSIGNEE_LAST_NAME = models.CharField(max_length=100, null=True)
	ASSIGNEE_FIRST_NAME = models.CharField(max_length=100, null=True)
	VEHICLE_CATEGORY = models.CharField(max_length=100, null=True)
	Employee_Id = models.ForeignKey('EmployeeMasterlist', on_delete=models.DO_NOTHING)
	#Employee_Id = models.CharField(max_length=100, null=True)
	BAND_LEVEL  = models.CharField(max_length=100, null=True)
	BENEFIT_GROUP = models.CharField(max_length=100, null=True)
	COST_CENTER = models.CharField(max_length=100, null=True)
	GROUP = models.CharField(max_length=100, null=True)
	DIVISION = models.CharField(max_length=100, null=True)
	DEPARTMENT = models.CharField(max_length=100, null=True)
	SECTION = models.CharField(max_length=100, null=True)
	IS_ID = models.CharField(max_length=100, null=True)
	IS_LAST_NAME = models.CharField(max_length=100, null=True)
	IS_FIRST_NAME = models.CharField(max_length=100, null=True)
	LOCATION = models.CharField(max_length=100, null=True)
	ORIGINAL_OR_DATE  = models.DateField(auto_now=False, null=True)
	ACQ_DATE  = models.DateField(auto_now=False, null=True)
	ACQ_COST = models.CharField(max_length=100, null=True)
	ASSET_NO = models.CharField(max_length=100, null=True)
	EQUIPMENT_NO = models.CharField(max_length=100, null=True)
	PO_NO = models.CharField(max_length=100, null=True)
	PLATE_NUMBER_RELEASE_DATE = models.DateField(auto_now=False, null=True)
	# Employee_Id = models.CharField(max_length=100, null=True)

	# Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	# No = models.CharField(max_length=50, null=True, default=increment_No)
	# Plate_no = models.CharField(max_length=50, null=True)
	# Conduction_Sticker = models.CharField(max_length=100, null=True)
	# Remarks = models.CharField(max_length=100, null=True)
	# CR_name = models.CharField(max_length=100, null=True)
	# Ending = models.CharField(max_length=20, null=True)
	# Model = models.CharField(max_length=50, null=True)
	# Brand = models.CharField(max_length=50, null=True, choices=Vbrand)
	# Vehicle_make = models.CharField(max_length=100, null=True)
	# Engine_No = models.CharField(max_length=100, null=True)
	# Chassis_no = models.CharField(max_length=100, null=True)
	# MV_file_no = models.CharField(max_length=100, null=True)
	# vehicle_type = models.CharField(max_length=100, null=True)
	# Vehicle_category = models.CharField(max_length=100, null=True)
	# Employee_Id = models.ForeignKey('EmployeeMasterlist', on_delete=models.DO_NOTHING)
	# Band_level = models.CharField(max_length=50, null=True)
	# Band_Benefit = models.CharField(max_length=50, null=True)
	# Contact_no = models.CharField(max_length=50, null=True)
	# Cost_center = models.CharField(max_length=100,null=True)
	# Group =models.CharField(max_length=100, null=True)
	# Division = models.CharField(max_length=100, null=True)
	# Department = models.CharField(max_length=100, null=True)
	# Section = models.CharField(max_length=100, null=True)
	# IS_employee_ID = models.CharField(max_length=100, null=True)
	# IS_firstname = models.CharField(max_length=100, null=True)
	# IS_lastname = models.CharField(max_length=100, null=True)
	# Location = models.CharField(max_length=100, null=True)
	# Aquisition_date = models.DateField(auto_now=False, null=True)
	# Aquisition_cost = models.CharField(max_length=100, null=True)
	# Asset_no = models.CharField(max_length=100, null=True)
	# PO_no = models.CharField(max_length=100, null=True)
	# SAP_PR = models.CharField(max_length=100, null=True)
	# Vehicle_IVN_no = models.CharField(max_length=100, null=True)
	# Unit_MATDOC = models.CharField(max_length=100, null=True)
	# Grdd_date = models.CharField(max_length=100, null=True)
	# Equipment_no = models.CharField(max_length=100, null=True)
	# Latest_registration = models.DateField(auto_now=False, null=True)
	# Lates_remark = models.CharField(max_length=100, null=True)
	# Lname_assignee = models.CharField(max_length=50, null=True)
	# Fname_assignee = models.CharField(max_length=50, null=True)
	# reg_month = models.CharField(max_length=50, null=True)
	# original_OR_date = models.DateField(auto_now=False, null=True)
	# plateNo_release = models.DateField(auto_now=False, null=True)

	def __str__(self):
		return self.PLATE_NO
		
	def get_absolute_url(self):
		return reverse('vehicle-list')





