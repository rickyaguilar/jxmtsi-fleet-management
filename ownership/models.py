from django.db import models
import datetime
from django.urls import reverse
from masterlist.models import VehicleMasterList
# History
from simple_history.models import HistoricalRecords

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
    date_application = models.DateField(auto_now=False, null=True, blank=True)
    req_employee_id = models.CharField(max_length=50, null=True, blank=True)
    req_Fname = models.CharField(max_length=100, null=True, blank=True)
    req_Lname =  models.CharField(max_length=100, null=True, blank=True)
    req_band = models.CharField(max_length=100, null=True, blank=True)
    req_cost =  models.CharField(max_length=100, null=True, blank=True)
    req_title = models.CharField(max_length=100, null=True, blank=True)
    # plate_no= models.ForeignKey('masterlist.VehicleMasterList', on_delete=models.DO_NOTHING)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    cond_sticker = models.CharField(max_length=100, null=True, blank=True)
    vehicle_model = models.CharField(max_length=100, null=True, blank=True)
    vehicle_brand = models.CharField(max_length=100, null=True, blank=True)
    vehicle_make = models.CharField(max_length=100, null=True, blank=True)
    vendor = models.CharField(max_length=100, null=True, choices=vendor, blank=True)
    vendor_name = models.CharField(max_length=100, null=True, blank=True)
    v_employee_id =  models.CharField(max_length=100, null=True, blank=True)
    v_fname = models.CharField(max_length=100, null=True, blank=True)
    v_lname = models.CharField(max_length=100, null=True, blank=True)
    v_band = models.CharField(max_length=100, null=True, blank=True)
    purpose = models.CharField(max_length=100, null=True, choices=purpose, blank=True)
    transfer_fee = models.CharField(max_length=100, null=True, blank=True)
    doc_date_completed =models.CharField(max_length=100, null=True, blank=True)
    deedofsale_date = models.CharField(max_length=100, null=True, blank=True)
    confirmation_status = models.CharField(max_length=100, null=True, choices=confirm, blank=True)
    emailed_to_casher =models.CharField(max_length=100, null=True, blank=True)
    received_from_casher =models.CharField(max_length=100, null=True, blank=True)
    deed_signed =models.CharField(max_length=100, null=True, blank=True)
    routed_to_jd =models.CharField(max_length=100, null=True, blank=True)
    approved_by_jd =models.CharField(max_length=100, null=True, blank=True)
    return_fleet_admin =models.CharField(max_length=100, null=True, blank=True)
    forwarded_to_liason =models.CharField(max_length=100, null=True, blank=True)
    date_notarized =models.CharField(max_length=100, null=True, blank=True)
    endorosed_to_insurance = models.CharField(max_length=100, null=True, blank=True)
    requested_for_pullout =models.CharField(max_length=100, null=True, blank=True)
    date_pulled =models.CharField(max_length=100, null=True, blank=True)
    return_endorsementfleet =models.CharField(max_length=100, null=True, blank=True)
    forwarded_fleet_liason =models.CharField(max_length=100, null=True, blank=True)
    tmg_date_in =models.CharField(max_length=100, null=True, blank=True)
    tmg_date_out =models.CharField(max_length=100, null=True, blank=True)
    tmg_date_return =models.CharField(max_length=100, null=True, blank=True)
    lto_date_in =models.CharField(max_length=100, null=True, blank=True)
    lto_date_out =models.CharField(max_length=100, null=True, blank=True)
    lto_date_return =models.CharField(max_length=100, null=True, blank=True)
    date_docs_return =models.CharField(max_length=100, null=True, blank=True)
    date_transfered_completed =models.CharField(max_length=100, null=True, blank=True)
    date_comletion_vismin =models.CharField(max_length=100, null=True, blank=True)

    TOO_SLA = models.CharField(max_length=10, null=True, blank=True)
    date_initiated = models.DateField(auto_now=True, null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.Activity_id


    def get_absolute_url(self):
        return reverse('ownership_list')




		