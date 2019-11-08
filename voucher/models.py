from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from datetime import date

def increment_Activity_id():
    	last_in = CarRentalRequest.objects.all().order_by('id').last()
	if not last_in:
	    return 'CRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'CRR' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id

class expense_voucher(models.Model):
    