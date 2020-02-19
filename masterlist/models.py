from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
# History
from simple_history.models import HistoricalRecords

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
	history = HistoricalRecords()

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
	PLATE_NO = models.CharField(max_length=100, null=True, blank=True)
	CS_NO = models.CharField(max_length=100, null=True, blank=True)
	CR_NAME = models.CharField(max_length=100, null=True, blank=True)
	PLATE_ENDING = models.CharField(max_length=1, null=True, blank=True)
	REGISTRATION_MONTH = models.CharField(max_length=5, null=True, blank=True)
	MODEL = models.CharField(max_length=10, null=True, blank=True)
	BRAND = models.CharField(max_length=100, null=True, choices=Vbrand)
	VEHICLE_MAKE = models.CharField(max_length=100, null=True, blank=True)
	ENGINE_NO = models.CharField(max_length=100, null=True, blank=True)
	CHASSIS_NO = models.CharField(max_length=100, null=True, blank=True)
	MV_FILE_NO = models.CharField(max_length=100, null=True, blank=True)
	VEHICLE_TYPE = models.CharField(max_length=100, null=True, blank=True)
	ASSIGNEE_LAST_NAME = models.CharField(max_length=100, null=True, blank=True)
	ASSIGNEE_FIRST_NAME = models.CharField(max_length=100, null=True, blank=True)
	VEHICLE_CATEGORY = models.CharField(max_length=100, null=True, blank=True)
	BAND_LEVEL  = models.CharField(max_length=100, null=True, blank=True)
	BENEFIT_GROUP = models.CharField(max_length=100, null=True, blank=True)
	COST_CENTER = models.CharField(max_length=100, null=True, blank=True)
	GROUP = models.CharField(max_length=100, null=True, blank=True)
	DIVISION = models.CharField(max_length=100, null=True, blank=True)
	DEPARTMENT = models.CharField(max_length=100, null=True, blank=True)
	SECTION = models.CharField(max_length=100, null=True, blank=True)
	IS_ID = models.CharField(max_length=100, null=True, blank=True)
	IS_LAST_NAME = models.CharField(max_length=100, null=True, blank=True)
	IS_FIRST_NAME = models.CharField(max_length=100, null=True, blank=True)
	LOCATION = models.CharField(max_length=100, null=True, blank=True)
	ORIGINAL_OR_DATE  = models.DateField(auto_now=False, null=True, blank=True)
	ACQ_DATE  = models.DateField(auto_now=False, null=True, blank=True)
	ACQ_COST = models.CharField(max_length=100, null=True, blank=True)
	ASSET_NO = models.CharField(max_length=100, null=True, blank=True)
	EQUIPMENT_NO = models.CharField(max_length=100, null=True, blank=True)
	PO_NO = models.CharField(max_length=100, null=True, blank=True)
	PLATE_NUMBER_RELEASE_DATE = models.DateField(auto_now=False, null=True, blank=True)
	Employee = models.CharField(max_length=100, null=True)
	history = HistoricalRecords()


	def __str__(self):
		return self.PLATE_NO
				
	def get_absolute_url(self):
		return reverse('vehicle-list')





