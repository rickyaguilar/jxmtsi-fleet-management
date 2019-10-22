from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Fata_monitoring




class FATAmonitoringForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FATAmonitoringForm, self).__init__(*args, **kwargs)
        self.fields['Certificate_of_Reg'].required = False
        self.fields['Vehicle_brand'].required = False
        self.fields['Vehicle_model'].required = False
        self.fields['Globe_fixed_asset'].required = False
        self.fields['Innove_fixed_asset'].required = False
        self.fields['Date_endorsed_Globe'].required = False
        self.fields['Date_endorsed_Innove'].required = False
        self.fields['Clearing_accountability'].required = False

    class Meta:
        model = Fata_monitoring
        fields = ['Fata_no','Date_transfer', 'Date_received', 'Plate_no', 'Vehicle_make','Vehicle_brand',
                    'Certificate_of_Reg','Vehicle_model','Transferor_employee','Transferor_Fname','Transferor_Lname',
                    'Recipient_Employee','Recipient_Fname','Recipient_Lname','Date_endorsed_Globe','Date_endorsed_Innove',
                    'Clearing_accountability','Globe_fixed_asset','Innove_fixed_asset']
                    
        widgets= {
            "Fata_no": forms.TextInput(attrs={'class':'form-control','type':'number'}),
            "Date_transfer": forms.TextInput(attrs={'class':'form-control','type':'date'}),
            "Date_received": forms.TextInput(attrs={'class':'form-control','type':'date'}),
            "Plate_no": forms.Select(attrs={'class':'form-control'}),
            "Vehicle_make": forms.TextInput(attrs={'class':'form-control'}),
            "Vehicle_brand": forms.TextInput(attrs={'class':'form-control'}),
            "Certificate_of_Reg": forms.TextInput(attrs={'class':'form-control'}),
            "Vehicle_model": forms.TextInput(attrs={'class':'form-control'}),
            "Transferor_employee": forms.TextInput(attrs={'class':'form-control'}),
            "Transferor_Fname": forms.TextInput(attrs={'class':'form-control'}),
            "Transferor_Lname": forms.TextInput(attrs={'class':'form-control'}),
            "Recipient_Employee": forms.TextInput(attrs={'class':'form-control'}),
            "Recipient_Fname": forms.TextInput(attrs={'class':'form-control'}),
            "Recipient_Lname": forms.TextInput(attrs={'class':'form-control'}),
            "Date_endorsed_Globe": forms.TextInput(attrs={'class':'form-control','type':'date'}),
            "Date_endorsed_Innove": forms.TextInput(attrs={'class':'form-control','type':'date'}),
            "Clearing_accountability": forms.TextInput(attrs={'class':'form-control'}),
            "Globe_fixed_asset": forms.TextInput(attrs={'class':'form-control'}),
            "Innove_fixed_asset": forms.TextInput(attrs={'class':'form-control'})

        }