from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
from masterlist.models import EmployeeMasterlist,VehicleMasterList

#<---CarRental Payment-->
def increment_Activity_id():
	last_in = CarRental.objects.all().order_by('id').last()
	if not last_in:
	    return 'CRP' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'CRP' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

def increment_I_number():
	last_in = CarRental.objects.all().order_by('id').last()
	if not last_in:
	    return 'I' + '000001'
	in_id = last_in.I_number
	in_int = int(in_id[5:])
	new_in_int = in_int + 1
	new_in_id = 'I' + str(new_in_int).zfill(6)
	return new_in_id

class CarRental(models.Model):
	#<-- assignee details---->
	Activity_id = models.CharField(max_length=100,null=True, default=increment_Activity_id)
	Bill_date = models.CharField(max_length=100, null=True)
	A_employee_Id = models.ForeignKey('masterlist.EmployeeMasterlist', on_delete=models.DO_NOTHING)
	# Employee_id = models.CharField(max_length=100, null=True)
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
	C_SLA = models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('carrental_list', kwargs={'pk':self.pk})


#<---Vehicle Payment--->
def increment_Activity_id():
	last_in = VehiclePayment.objects.all().order_by('id').last()
	if not last_in:
	    return 'NVP' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[12:])
	new_in_int = in_int + 1
	new_in_id = 'NVP' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id


def increment_PO_no():
	last_in = VehiclePayment.objects.all().order_by('id').last()
	if not last_in:
	    return '000000001'
	in_id = last_in.PO_no
	in_int = int(in_id[5:])
	new_in_int = in_int + 1
	new_in_id = str(new_in_int).zfill(9)
	return new_in_id

class VehiclePayment(models.Model):
	Activity_id = models.CharField(max_length=20, default=increment_Activity_id)
	PO_no = models.CharField(max_length=100, default=increment_PO_no)
	A_employee_ID = models.ForeignKey('masterlist.EmployeeMasterlist', on_delete=models.DO_NOTHING)
	# A_employee_ID = models.CharField(max_length=100, null=True)
	E_First_name = models.CharField(max_length=50, blank=True)
	E_Last_name = models.CharField(max_length=50, blank=True)
	V_deliverDate = models.DateField(auto_now=False, null=True)
	Plate_no = models.ForeignKey('masterlist.VehicleMasterList', on_delete=models.DO_NOTHING)
	# V_plateNo = models.CharField(max_length=20, blank=True)
	V_model = models.CharField(max_length=100, blank=True)
	V_brand = models.CharField(max_length=100, blank=True)
	V_make = models.CharField(max_length=100, blank=True)
	V_dealer = models.CharField(max_length=100, blank=True)
	LTO_documents = models.DateField(auto_now=False, null=True)
	Docs_plate_no = models.CharField(max_length=50, blank=True)
	LTO_stickers = models.CharField(max_length=100, blank=True)
	Sticker_fields = models.CharField(max_length=100, blank=True)
	Date_initial = models.DateField(auto_now=False, null=True)
	First_payment = models.CharField(max_length=100, blank=True)
	LTO_charges = models.CharField(max_length=100, blank=True)
	Outstanding_balance = models.CharField(max_length=100, blank=True)
	Date_final = models.DateField(auto_now=False, null=True)
	Routing_remarks = models.CharField(max_length=100, blank=True)
	V_SLA = models.CharField(max_length=10, blank=True)
	Next_process = models.CharField(max_length=100, blank=True)
	Date_initiated = models.DateField(auto_now=True)

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('Vehicle_list')

#<---Fuel Supplier Payment--->
def increment_Activity_id():
	last_in = Fuel_supplier.objects.all().order_by('id').last()
	if not last_in:
	    return 'SOA' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'SOA' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id


class Fuel_supplier(models.Model):
	PAYEE = (
		('Globe', 'Globe'),
		('Innove', 'Innove'),
		('Byan', 'Bayan'),
	)

	Activity_id = models.CharField(max_length=20,null=True, default=increment_Activity_id)
	SOA_Date_received = models.DateField(auto_now=False, null=True)
	Fuel_provider = models.CharField(max_length=50, null=True)
	SOA_billdate = models.DateField(auto_now=False, null=True)
	SOA_current_amount = models.CharField(max_length=50, null=True)
	SOA_outstanding_amount = models.CharField(max_length=50, null=True)
	Payee = models.CharField(max_length=10, null=True, choices=PAYEE)
	SOA_attached = models.CharField(max_length=100, null=True)
	Date_initiated = models.DateField(auto_now=True)
	Payment_deadline = models.DateField(auto_now=False, null=True)
	Date_forwarded = models.DateField(auto_now=False, null=True)
	F_SLA = models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.Activity_id

	def get_absolute_url(self):
		return reverse('Fuel_supplierList')






