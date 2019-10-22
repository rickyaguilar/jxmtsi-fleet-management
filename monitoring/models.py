
from django.db import models
from django.utils import timezone
import datetime
from datetime import date
from django.urls import reverse
from masterlist.models import VehicleMasterList

def increment_Activity_id():
	last_in = Fata_monitoring.objects.all().order_by('id').last()
	if not last_in:
	    return 'FM' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'FM' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id


class Fata_monitoring(models.Model):
	Activity_id = models.CharField(max_length=100, default=increment_Activity_id)
	Fata_no = models.CharField(max_length=100, null=True)
	Date_transfer = models.DateField(auto_now=False, null=True)
	Date_received = models.DateField(auto_now=False, null=True)
	Plate_no = models.ForeignKey('masterlist.VehicleMasterList', on_delete=models.DO_NOTHING)
	Vehicle_make = models.CharField(max_length=100, null=True)
	Vehicle_brand = models.CharField(max_length=100, null=True)
	Certificate_of_Reg = models.CharField(max_length=100, null=True)
	Vehicle_model = models.CharField(max_length=100, null=True)
	# Transferor_employee = models.ForeignKey('masterlist.EmployeeMasterlist', on_delete=models.DO_NOTHING)
	Transferor_employee = models.CharField(max_length=100, null=True)
	Transferor_Fname = models.CharField(max_length=100, null=True)
	Transferor_Lname =  models.CharField(max_length=100, null=True)
	Recipient_Employee = models.CharField(max_length=100, null=True)
	Recipient_Fname = models.CharField(max_length=100, null=True)
	Recipient_Lname = models.CharField(max_length=100, null=True)
	Date_endorsed_Globe = models.DateField(auto_now=False, null=True)
	Date_endorsed_Innove = models.DateField(auto_now=False, null=True)
	Clearing_accountability = models.CharField(max_length=10, null=True)
	Globe_fixed_asset = models.CharField(max_length=50, null=True)
	Innove_fixed_asset = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.Activity_id


	def get_absolute_url(self):
		return reverse('Monitoring_list')




		