from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date


def increment_Activity_id():
	last_in = CarRental.objects.all().order_by('id').last()
	if not last_in:
	    return 'CRP' + str(datetime.datetime.today().strftime('%Y')) + '-' + '0001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'CRP' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(4)
	return new_in_id



def increment_I_number():
	last_in = CarRental.objects.all().order_by('id').last()
	if not last_in:
	    return '000001'
	in_id = last_in.I_number
	in_int = int(in_id[5:])
	new_in_int = in_int + 1
	new_in_id = 'I' + str(new_in_int).zfill(6)
	return new_in_id

class CarRental(models.Model):
	#<-- assignee details---->
	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	Bill_date = models.DateField(auto_now=False, null=True)
	Employee_id = models.CharField(max_length=100, null=True)
	L_name = models.CharField(max_length=100, null=True)
	F_name = models.CharField(max_length=100, null=True)
	Assignee_company = models.CharField(max_length=100, null=True)
	Cost_center = models.CharField(max_length=100, null=True)
	Date_initiated = models.DateField(auto_now=False)
	#<--other assignee---->
	O_Fname = models.CharField(max_length=100, null=True)
	O_Lname = models.CharField(max_length=100, null=True)
	O_cost_center = models.CharField(max_length=100, null=True)
	#<---Vehicle Details-->
	Plate_no = models.CharField(max_length=100, null=True)
	V_provider = models.CharField(max_length=100, null=True)
	V_brand = models.CharField(max_length=100, null=True)
	V_make = models.CharField(max_length=100, null=True)
	#<---Rental Details--->
	D_vehicle = models.CharField(max_length=100, null=True)
	S_rental = models.CharField(max_length=100, null=True)
	E_rental = models.CharField(max_length=100, null=True)
	R_duration = models.CharField(max_length=100, null=True)
	#<---Expense Details--->
	R_Cost = models.CharField(max_length=100, null=True)
	G_cost = models.CharField(max_length=100, null=True)
	T_fee = models.CharField(max_length=100, null=True)
	P_fee = models.CharField(max_length=100, null=True)
	Del_fee = models.CharField(max_length=100, null=True)
	Dri_fee = models.CharField(max_length=100, null=True)
	M_cost = models.CharField(max_length=100, null=True)
	O_expenses = models.CharField(max_length=100, null=True)
	VAT = models.CharField(max_length=100, null=True)
	T_expenses = models.CharField(max_length=100, null=True)
	#<-- Other Rental-->
	I_number = models.CharField(max_length=100, null=True, default=increment_I_number)
	I_amount = models.CharField(max_length=100, null=True)
	R_purpose = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('carrental_list', kwargs={'pk':self.pk})

#class Car(models.Model):

#	car_id = models.CharField(max_length=100, default=increment_car_id)
#	car_brand = models.CharField(max_length=100)
#	car_model = models.CharField(max_length=100, null=True)
#	car_plate = models.CharField(max_length=100)

#	def __str__(self):
#		return self.car_id

#	def get_absolute_url(self):
#		return reverse('Car-new', kwargs={'pk':self.pk})






