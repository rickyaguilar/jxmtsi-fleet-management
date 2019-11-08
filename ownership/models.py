
from django.db import models
import datetime
from django.urls import reverse

def increment_Activity_id():
	last_in = Ownership.objects.all().order_by('id').last()
	if not last_in:
	    return 'TOO' + str(datetime.datetime.today().strftime('%Y')) + '-' + '000001'
	in_id = last_in.Activity_id
	in_int = int(in_id[10:])
	new_in_int = in_int + 1
	new_in_id = 'TOO' + str(datetime.datetime.today().strftime('%Y')) + '-' + str(new_in_int).zfill(6)
	return new_in_id


class Ownership(models.Model):
    vendor=(
        ('Globe Telecome','Globe Telecome'),
        ('Innove','Innove'),
        ('Bayantel Communication','Bayantel Communication'),
    )
    purpose=(
        ('Deceased','Deceased'),
        ('Early Availment','Early Availment'),
        ('End of Car Plan','End of Car Plan'),
        ('FSSV Availment','FSSV Availment'),
        ('Promotion','Promotion'),
        ('Resigned','Resigned'),
        ('Shift from Non-Sales to Sales','Shift from Non-Sales to Sales'),
        ('Shift from Sales to Non-Sales','Shift from Sales to Non-Sales'),
        ('Winning Bidder','Winning Bidder'),
    )
    confirm=(
        ('Confirmed','Confirmed'),
        ('Final Pay','Final Pay'),
    )
    Activity_id = models.CharField(max_length=100, default=increment_Activity_id)
    date_application = models.DateField(auto_now=False, null=True)
    req_employee_id = models.CharField(max_length=50, null=True)
    req_Fname = models.CharField(max_length=100, null=True)
    req_Lname =  models.CharField(max_length=100, null=True)
    req_band = models.CharField(max_length=100, null=True)
    req_cost =  models.CharField(max_length=100, null=True)
    req_title = models.CharField(max_length=100, null=True)
    plate_no = models.CharField(max_length=100, null=True)
    cond_sticker = models.CharField(max_length=100, null=True)
    vehicle_model = models.CharField(max_length=100, null=True)
    vehicle_brand = models.CharField(max_length=100, null=True)
    vehicle_make = models.CharField(max_length=100, null=True)
    vendor = models.CharField(max_length=100, null=True, choices=vendor)
    vendor_name = models.CharField(max_length=100, null=True)
    v_employee_id =  models.CharField(max_length=100, null=True)
    v_fname = models.CharField(max_length=100, null=True)
    v_lname = models.CharField(max_length=100, null=True)
    v_band = models.CharField(max_length=100, null=True)
    purpose = models.CharField(max_length=100, null=True, choices=purpose)
    transfer_fee = models.CharField(max_length=100, null=True)
    doc_date_completed = models.DateField(auto_now=False, null=True)
    deedofsale_date =  models.DateField(auto_now=False, null=True)
    confirmation_status = models.CharField(max_length=100, null=True, choices=confirm)
    emailed_to_casher = models.DateField(auto_now=False, null=True)
    received_from_casher = models.DateField(auto_now=False, null=True)
    deed_signed = models.DateField(auto_now=False, null=True)
    routed_to_jd = models.DateField(auto_now=False, null=True)
    approved_by_jd = models.DateField(auto_now=False, null=True)
    return_fleet_admin = models.DateField(auto_now=False, null=True)
    forwarded_to_liason = models.DateField(auto_now=False, null=True)
    date_notarized = models.DateField(auto_now=False, null=True)
    endorosed_to_insurance =  models.DateField(auto_now=False, null=True)
    requested_for_pullout = models.DateField(auto_now=False, null=True)
    date_pulled = models.DateField(auto_now=False, null=True)
    return_endorsementfleet = models.DateField(auto_now=False, null=True)
    forwarded_fleet_liason = models.DateField(auto_now=False, null=True)
    tmg_date_in = models.DateField(auto_now=False, null=True)
    tmg_date_out = models.DateField(auto_now=False, null=True)
    tmg_date_return = models.DateField(auto_now=False, null=True)
    lto_date_in = models.DateField(auto_now=False, null=True)
    lto_date_out = models.DateField(auto_now=False, null=True)
    lto_date_return = models.DateField(auto_now=False, null=True)

    date_docs_return = models.DateField(auto_now=False, null=True)
    date_transfered_completed = models.DateField(auto_now=False, null=True)
    date_comletion_vismin = models.DateField(auto_now=False, null=True)

    TOO_SLA = models.CharField(max_length=10, null=True)
    date_initiated = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.Activity_id


    def get_absolute_url(self):
        return reverse('ownership_list')




		