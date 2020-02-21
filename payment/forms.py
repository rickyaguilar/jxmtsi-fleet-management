from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import VehiclePayment,Fuel_supplier


class VehiclePaymentform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(VehiclePaymentform, self).__init__(*args, **kwargs)
		self.fields['LTO_documents'].required = False
		self.fields['Docs_plate_no'].required = False
		self.fields['LTO_stickers'].required = False
		self.fields['Sticker_fields'].required = False
		self.fields['Date_initial'].required = False
		self.fields['First_payment'].required = False
		self.fields['LTO_charges'].required = False
		self.fields['Outstanding_balance'].required = False
		self.fields['Date_final'].required = False
		self.fields['Routing_remarks'].required = False
		
	class Meta:
		model = VehiclePayment
		fields = ['A_employee_ID', 'E_First_name', 'E_Last_name', 'V_deliverDate','Plate_no',
		            'V_model','V_brand','V_make','V_dealer','LTO_documents',
		            'Docs_plate_no','LTO_stickers','Sticker_fields','Date_initial', 'First_payment', 'LTO_charges',
		            'Outstanding_balance','Date_final','Routing_remarks','V_SLA']
		widgets = {
			'A_employee_ID': forms.Select(attrs={'class':'form-control'}),
			'E_First_name': forms.TextInput(attrs={'class':'form-control'}),
			'E_Last_name': forms.TextInput(attrs={'class':'form-control'}),
			'V_deliverDate': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'Plate_no': forms.TextInput(attrs={'class':'form-control'}),
		    'V_model': forms.TextInput(attrs={'class':'form-control'}),
		    'V_brand': forms.TextInput(attrs={'class':'form-control'}),
		    'V_make': forms.TextInput(attrs={'class':'form-control'}),
		    'V_dealer': forms.TextInput(attrs={'class':'form-control'}),
		    'LTO_documents': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		    'Docs_plate_no': forms.Select(attrs={'class':'form-control'}),
		    'LTO_stickers': forms.TextInput(attrs={'class':'form-control'}),
		    'Sticker_fields': forms.TextInput(attrs={'class':'form-control'}),
		    'Date_initial': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
		    'First_payment': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		    'LTO_charges': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		    'Outstanding_balance': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		    'Date_final': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		    'Routing_remarks': forms.TextInput(attrs={'class':'form-control'}),
		    'V_SLA': forms.TextInput(attrs={'class':'form-control','type':'number','value':'15','hidden':'True'})
		}

class FuelsupplierForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(FuelsupplierForm, self).__init__(*args, **kwargs)
		self.fields['Fuel_provider'].required = False
		self.fields['SOA_current_amount'].required = False
		self.fields['SOA_outstanding_amount'].required = False
		self.fields['Payee'].required = False
		self.fields['SOA_attached'].required = False
		self.fields['Payment_deadline'].required = False
		self.fields['Date_forwarded'].required = False
		self.fields['F_SLA'].required = False

	class Meta:
		model = Fuel_supplier
		fields = [
		'SOA_Date_received','Fuel_provider','SOA_billdate','SOA_current_amount','SOA_outstanding_amount'
		,'Payee','SOA_attached','Payment_deadline','Date_forwarded','F_SLA'
		]

		CHOICES= (
			('GLOBE', 'GLOBE'),
			('INNOVE', 'INNOVE'),
			('BAYAN', 'BAYAN'),
		)
		widgets = {

		'SOA_Date_received': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'Fuel_provider': forms.TextInput(attrs={'class':'form-control'}),
		'SOA_billdate': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'SOA_current_amount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'SOA_outstanding_amount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
		'Payee': forms.Select(attrs={'class':'form-control','choices':'CHOICES'}),
		'SOA_attached': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
		'Payment_deadline': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'Date_forwarded': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'F_SLA': forms.TextInput(attrs={'class':'form-control','type':'number','value':'15','hidden':'True'})
		}







