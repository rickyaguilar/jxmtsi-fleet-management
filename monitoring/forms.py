from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Fata_monitoring




class FATAmonitoringForm(forms.ModelForm):
    class Meta:
        model = Fata_monitoring
        fields = ['Date_transfer', 'Date_received', 'Plate_no', 'Vehicle_make','Vehicle_brand',
                    'Certificate_of_Reg','Vehicle_model','Transferor_employee','Transferor_Fname','Transferor_Lname',
                    'Recipient_Employee','Recipient_Fname','Recipient_Lname']
        label = {
            "Date_transfer": "Date Transfer",
            "Date_received": "Date Received",
            "Plate_no": "Plate Number",
            "Vehicle_make": "Vehicle Make",
            "Vehicle_brand": "Vehicle Brand",
            "Certificate_of_Reg": "Certificate Of Registrations",
            "Vehicle_model": "Vehicle Model",
            "Transferor_employee": "Transferor Employee",
            "Transferor_Fname": "Transferor First Name",
            "Transferor_Lname": "Transferor Lastn Name",
            "Recipient_Employee":"Recipient Employee",
            "Recipient_Fname": "Recipient First Name",
            "Recipient_Lname": "Recipient Last Name",

        }