from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import VehiclePayment




class VehiclePaymentform(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(VehiclePaymentform, self).__init__(*args, **kwargs)
		self.fields['LTO_documents'].required = False
		self.fields['Date_final'].required = False
		self.fields['Date_initial'].required = False
		
	class Meta:
		model = VehiclePayment
		fields = ['A_employee_ID', 'E_First_name', 'E_Last_name', 'V_deliverDate','V_plateNo',
		            'V_model','V_brand','V_make','V_dealer','LTO_documents',
		            'Docs_plate_no','LTO_stickers','Sticker_fields','Date_initial', 'First_payment', 'LTO_charges',
		            'Outstanding_balance','Date_final','Routing_remarks','V_SLA']
		widgets = {
			'A_employee_ID': forms.TextInput(attrs={'class':'form-control'}),
			'E_First_name': forms.TextInput(attrs={'class':'form-control'}),
			'E_Last_name': forms.TextInput(attrs={'class':'form-control'}),
			'V_deliverDate': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'V_plateNo': forms.TextInput(attrs={'class':'form-control'}),
		    'V_model': forms.TextInput(attrs={'class':'form-control'}),
		    'V_brand': forms.TextInput(attrs={'class':'form-control'}),
		    'V_make': forms.TextInput(attrs={'class':'form-control'}),
		    'V_dealer': forms.TextInput(attrs={'class':'form-control'}),
		    'LTO_documents': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		    'Docs_plate_no': forms.TextInput(attrs={'class':'form-control'}),
		    'LTO_stickers': forms.TextInput(attrs={'class':'form-control'}),
		    'Sticker_fields': forms.TextInput(attrs={'class':'form-control'}),
		    'Date_initial': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
		    'First_payment': forms.TextInput(attrs={'class':'form-control'}),
		    'LTO_charges': forms.TextInput(attrs={'class':'form-control'}),
		    'Outstanding_balance': forms.TextInput(attrs={'class':'form-control'}),
		    'Date_final': forms.TextInput(attrs={'class':'form-control','type':'date'}),
		    'Routing_remarks': forms.TextInput(attrs={'class':'form-control'}),
		    'V_SLA': forms.TextInput(attrs={'class':'form-control'})
		}

# class CarRentalForm(forms.ModelForm):
# 	class Meta:
# 		model = CarRental

# 		fields = ['Bill_date','Employee_id','L_name','F_name','Cost_center','Date_initiated',
# 				'O_Fname','O_Lname','O_cost_center','Plate_no','V_provider','V_brand','V_make',
# 				'D_vehicle','S_rental','E_rental','R_duration','R_Cost','G_cost','T_fee',
# 				'P_fee','Del_fee','Dri_fee','M_cost','O_expenses','T_expenses','I_amount',
# 				'R_purpose','C_SLA'
# 		]
# 		widgets = {
# 			'Bill_date': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
# 			'Employee_id':forms.TextInput(attrs={'class':'form-control'}),
# 			'L_name':forms.TextInput(attrs={'class':'form-control'}),
# 			'F_name':forms.TextInput(attrs={'class':'form-control'}),
# 			'Cost_center':forms.TextInput(attrs={'class':'form-control'}),
# 			'Date_initiated':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
# 			'O_Fname':forms.TextInput(attrs={'class':'form-control'}),
# 			'O_Lname':forms.TextInput(attrs={'class':'form-control'}),
# 			'O_cost_center':forms.TextInput(attrs={'class':'form-control'}),
# 			'Plate_no':forms.TextInput(attrs={'class':'form-control'}),
# 			'V_provider':forms.TextInput(attrs={'class':'form-control'}),
# 			'V_brand':forms.TextInput(attrs={'class':'form-control'}),
# 			'V_make':forms.TextInput(attrs={'class':'form-control'}),
# 			'D_vehicle':forms.TextInput(attrs={'class':'form-control'}),
# 			'S_rental':forms.TextInput(attrs={'class':'form-control'}),
# 			'E_rental':forms.TextInput(attrs={'class':'form-control'}),
# 			'R_duration':forms.TextInput(attrs={'class':'form-control'}),
# 			'R_Cost':forms.TextInput(attrs={'class':'form-control'}),
# 			'G_cost':forms.TextInput(attrs={'class':'form-control'}),
# 			'T_fee':forms.TextInput(attrs={'class':'form-control'}),
# 			'P_fee':forms.TextInput(attrs={'class':'form-control'}),
# 			'Del_fee':forms.TextInput(attrs={'class':'form-control'}),
# 			'Dri_fee':forms.TextInput(attrs={'class':'form-control'}),
# 			'M_cost':forms.TextInput(attrs={'class':'form-control'}),
# 			'O_expenses':forms.TextInput(attrs={'class':'form-control'}),
# 			'T_expenses':forms.TextInput(attrs={'class':'form-control'}),
# 			'I_amount':forms.TextInput(attrs={'class':'form-control'}),
# 			'R_purpose':forms.TextInput(attrs={'class':'form-control'}),
# 			'C_SLA':forms.TextInput(attrs={'class':'form-control'})
# 		}