from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date
from masterlist.models import EmployeeMasterlist

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





