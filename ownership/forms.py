from django import forms
from .models import Ownership




class ownershipForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ownershipForm, self).__init__(*args, **kwargs)
        self.fields['req_Fname'].required = False
        self.fields['req_Lname'].required = False
        self.fields['req_band'].required = False
        self.fields['req_cost'].required = False
        self.fields['req_title'].required = False
        self.fields['v_fname'].required = False
        self.fields['cond_sticker'].required = False
        self.fields['vehicle_model'].required = False
        self.fields['vehicle_brand'].required = False
        self.fields['v_lname'].required = False
        self.fields['vendor'].required = False
        self.fields['vendor_name'].required = False
        self.fields['v_employee_id'].required = False
        self.fields['v_band'].required = False
        self.fields['purpose'].required = False
        self.fields['transfer_fee'].required = False
        self.fields['doc_date_completed'].required = False
        self.fields['deedofsale_date'].required = False
        self.fields['confirmation_status'].required = False
        self.fields['emailed_to_casher'].required = False
        self.fields['received_from_casher'].required = False
        self.fields['deed_signed'].required = False
        self.fields['routed_to_jd'].required = False
        self.fields['vehicle_model'].required = False
        self.fields['vehicle_brand'].required = False
        self.fields['routed_to_jd'].required = False
        self.fields['approved_by_jd'].required = False
        # self.fields['return_fleet_admin'].required = False
        self.fields['forwarded_to_liason'].required = False
        self.fields['tmg_date_in'].required = False
        self.fields['tmg_location'].required = False
        self.fields['tmg_date_return'].required = False       
        self.fields['lto_date_in'].required = False
        self.fields['lto_date_out'].required = False
        self.fields['date_received_by'].required = False
        # self.fields['lto_date_return'].required = False
        # self.fields['date_docs_return'].required = False
        self.fields['date_transfered_completed'].required = False
        self.fields['date_comletion_vismin'].required = False
        self.fields['TOO_SLA'].required = False
        self.fields['date_notarized'].required = False
        self.fields['endorosed_to_insurance'].required = False
        self.fields['requested_for_pullout'].required = False
        # self.fields['date_pulled'].required = False
        self.fields['return_endorsementfleet'].required = False
        self.fields['forwarded_fleet_liason'].required = False
        self.fields['lto_location'].required = False

    class Meta:
        model = Ownership
        fields = ['date_application','req_employee_id', 'req_Fname', 'req_Lname', 'req_band','req_cost',
                    'req_title','plate_no','cond_sticker','vehicle_model','vehicle_brand','vehicle_make','vendor',
                    'vendor_name','v_employee_id','v_fname','v_lname','v_band','purpose','transfer_fee','doc_date_completed',
                    'deedofsale_date','confirmation_status','emailed_to_casher','received_from_casher',
                    'deed_signed','routed_to_jd','approved_by_jd','return_fleet_admin','forwarded_to_liason','date_notarized',
                    'endorosed_to_insurance','requested_for_pullout','forwarded_fleet_liason',
                    'tmg_date_in','tmg_location','tmg_date_return' ,'lto_date_in','lto_date_out', 'lto_location',
                    'date_transfered_completed','date_comletion_vismin','TOO_SLA', 'date_received_by',]
                    
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
        Location = (
            ('Manila East','Manila East'),
            ('Manila West','Manila West'),
            ('Manila South','Manila South'),
            ('Manila North','Manila North'),
            ('Navotas','Navotas'),
            ('Aguinaldo','Aguinaldo'),
            ('Las Pinas','Las Pinas'),
            ('Muntinlupa','Muntinlupa'),
            ('Paranaque','Paranaque'),
            ('Quezon City','Quezon City'),
            ('Taguig','Taguig'),
            ('Pasay','Pasay'),
            ('Novaliches','Novaliches'),
            ('Pasig','Pasig'),
            ('Caloocan','Caloocan'),
            ('Marikina','Marikina'),
            ('Mandaluyong','Mandaluyong'),
            ('San Juan','San Juan'),
            ('Diliman','Diliman'),
            ('Others','Others'),

        )
        widgets= {
            
            'date_application': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'req_employee_id': forms.TextInput(attrs={'class':'form-control'}),
            'req_Fname': forms.TextInput(attrs={'class':'form-control'}),
            'req_Lname': forms.TextInput(attrs={'class':'form-control'}),
            'req_band': forms.TextInput(attrs={'class':'form-control'}),
            'req_cost': forms.TextInput(attrs={'class':'form-control'}),
            'req_title': forms.TextInput(attrs={'class':'form-control'}),
            'plate_no': forms.Select(attrs={'class':'form-control'}),
            'cond_sticker' : forms.TextInput(attrs={'class':'form-control'}),
            'vehicle_model' : forms.TextInput(attrs={'class':'form-control'}),
            'vehicle_brand' : forms.TextInput(attrs={'class':'form-control'}),
            'vehicle_make' : forms.TextInput(attrs={'class':'form-control'}),
            'vendor' : forms.Select(attrs={'class':'form-control','choices':'vendor'}),
            'vendor_name' : forms.TextInput(attrs={'class':'form-control'}),
            'v_employee_id' : forms.TextInput(attrs={'class':'form-control'}),
            'v_fname' : forms.TextInput(attrs={'class':'form-control'}),
            'v_lname' : forms.TextInput(attrs={'class':'form-control'}),
            'v_band' : forms.TextInput(attrs={'class':'form-control'}),
            'purpose' : forms.Select(attrs={'class':'form-control','choices':'purpose'}),
            'transfer_fee' : forms.TextInput(attrs={'class':'form-control'}),
            'doc_date_completed' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'deedofsale_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'confirmation_status' : forms.Select(attrs={'class':'form-control','choices':'confirm'}),
            'emailed_to_casher' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'received_from_casher' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'deed_signed' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'routed_to_jd' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'approved_by_jd' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'return_fleet_admin' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'forwarded_to_liason' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'date_notarized' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'endorosed_to_insurance': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'requested_for_pullout' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            # 'date_pulled' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            # 'return_endorsementfleet' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'forwarded_fleet_liason' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'tmg_date_in' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'tmg_location' : forms.TextInput(attrs={'class':'form-control'}),
            'tmg_date_return' : forms.TextInput(attrs={'class':'form-control','type':'date'}),        
            'lto_date_in' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'lto_location' : forms.TextInput(attrs={'class':'form-control','choices':'Location'}),

            # 'lto_date_return': forms.TextInput(attrs={'class':'form-control','type':'date'}),
            # 'date_docs_return' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'date_transfered_completed' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'date_comletion_vismin' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'date_received_by' : forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'TOO_SLA' : forms.TextInput(attrs={'class':'form-control','value':'30','hidden':'true'}),

        }