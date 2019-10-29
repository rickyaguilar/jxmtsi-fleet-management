from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import CarRentalRequest, Gas_card



class carrequestform(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(carrequestform, self).__init__(*args, **kwargs)
		self.fields['Time'].required = False
		self.fields['Assignee_ATD'].required = False
		self.fields['Assignee_Section'].required = False
		self.fields['Assignee_band'].required = False
		self.fields['Type_of_vehicle'].required = False
		self.fields['Plate_no'].required = False
		self.fields['Immediate_supervisor'].required = False
		self.fields['Up_to'].required = False
		
	class Meta:
		model = CarRentalRequest
		fields = [
				'A_Employee_Id','Date_received','Assignee_Fname','Assignee_Lname','Assignee_No',
				'Assignee_Company','Assignee_band','Assignee_Dept','Assignee_Cost','Assignee_Div','Assignee_Loc',
				'Assignee_Section','Assignee_Designation','Assignee_ATD','Vendor_name','Date','Up_to','Time',
				'Place_of_del','type_rental','Cost_center','Rental_period','Destination','Delivery_date',
				'End_user','Type_of_vehicle','Plate_no','Immediate_supervisor','CR_SLA'
		]
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
		widgets = {
				'A_Employee_Id' : forms.Select(attrs={'class':'form-control'}),
				'Date_received': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
				'Assignee_Fname': forms.TextInput(attrs={'class':'form-control'}),
				'Assignee_Lname': forms.TextInput(attrs={'class':'form-control'}),
				'Assignee_No': forms.TextInput(attrs={'class':'form-control','type':'tel'}),
				'Assignee_Company': forms.TextInput(attrs={'class':'form-control'}),
				'Assignee_band': forms.TextInput(attrs={'class':'form-control'}),
				'Assignee_Dept': forms.TextInput(attrs={'class':'form-control'}),
				'Assignee_Cost': forms.TextInput(attrs={'class':'form-control','type':'number'}),
				'Assignee_Div' : forms.TextInput(attrs={'class':'form-control'}),
				'Assignee_Loc': forms.TextInput(attrs={'class':'form-control'}),
				'Assignee_Section': forms.TextInput(attrs={'class':'form-control'}),
				'Assignee_Designation': forms.TextInput(attrs={'class':'form-control'}),
				'Assignee_ATD': forms.TextInput(attrs={'class':'form-control'}),
				'Vendor_name': forms.TextInput(attrs={'class':'form-control'}),
				'Date' : forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
				'Up_to': forms.TextInput(attrs={'class':'form-control'}),
				'Time' : forms.TextInput(attrs={'class':'form-control', 'type':'time'}),
				'Place_of_del': forms.TextInput(attrs={'class':'form-control'}),
				'type_rental': forms.Select(attrs={'class':'form-control','choices':'Rental'}),
				# 'type_rental': forms.ChoiceField(widget=forms.RadioSelect, 'choices':'rental'),
				'Cost_center': forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
				'Rental_period' : forms.TextInput(attrs={'class':'form-control'}),
				'Destination' : forms.TextInput(attrs={'class':'form-control'}),
				'Delivery_date': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
				'End_user': forms.TextInput(attrs={'class':'form-control'}),
				'Type_of_vehicle': forms.Select(attrs={'class':'form-control', 'choices':'Vtype'}),
				'Plate_no': forms.TextInput(attrs={'class':'form-control'}),
				'Immediate_supervisor': forms.Select(attrs={'class':'form-control','choices':'CHOICES'}),
				'CR_SLA' : forms.TextInput(attrs={'class':'form-control','value':'2','hidden':'true'})
		}


class gascardform(forms.ModelForm):
    
	def __init__(self, *args, **kwargs):
		super(gascardform, self).__init__(*args, **kwargs)
		self.fields['approved_by'].required = False
		self.fields['date_summitted'].required = False
		self.fields['fleet_received'].required = False
		self.fields['fleet_card_no'].required = False
		self.fields['fleet_date_release'].required = False
		self.fields['person_release'].required = False
		self.fields['fleet_provider'].required = False
		self.fields['atd_no'].required = False
		self.fields['temporary_atd'].required = False
		self.fields['new_emp_id'].required = False
		self.fields['new_emp_fname'].required = False
		self.fields['new_emp_lname'].required = False
		self.fields['new_emp_cost'].required = False
		self.fields['new_temp_atd'].required = False
		self.fields['new_assignee'].required = False
		self.fields['cost_center_code'].required = False
		self.fields['cancellation'].required = False
		self.fields['plate_no'].required = False
		self.fields['con_sticker'].required = False
		self.fields['model_year'].required = False
		self.fields['brand'].required = False
		self.fields['make'].required = False
		self.fields['fuel_type'].required = False
		self.fields['new_plate_no'].required = False
		self.fields['new_cond_sticker'].required = False
		self.fields['new_model_year'].required = False
		self.fields['new_vbrand'].required = False
		self.fields['new_vmake'].required = False
		self.fields['new_vfuel_type'].required = False
		self.fields['GCR_SLA'].required = False
	class Meta:
		model = Gas_card
		fields = [
				'date_received','application_type','fleet_provider','fleetcard_type',
				'fuel_limit_amount','fuel_limit_quantity','products_restriction','req_employee_id','req_fname','req_lname','req_title',
				'req_cost_center','atd_no','temporary_atd','new_emp_id','new_emp_fname','new_emp_lname','new_emp_cost',
				'new_temp_atd','new_assignee','cost_center_code','cancellation','plate_no','con_sticker','model_year','brand','make',
				'fuel_type','new_plate_no','new_cond_sticker','new_model_year','new_vbrand','new_vmake','new_vfuel_type',
				'approved_by','date_summitted','fleet_received','fleet_card_no','fleet_date_release','person_release','GCR_SLA'
		]
			
		card_type= (
			('Single', 'Single'),
			('Driver','Driver'),
			('Vehicle','Vehicle'),
			)
		fleet_card= (
			('Petron', 'Petron'),
			('Shell','Shell'),
		)
		app_type= (
			('New Card', 'Daily'),
			('Transfer Acountability', 'Transfer Acountability'),
			('Cancel - Disposal of Vehicle', 'Cancel - Disposal of Vehicle'),
			('Cancel - Resignation of User', 'Cancel - Resignation of User'),
			('Replacement - Damage', 'Replacement - Damage'),
			('Replacement - Lose', 'Replacement - Lose'),
			('Others - Adjust Credit Limit', 'Others - Adjust Credit Limit'),
			('Others - Change of Product Restriction', 'Others - Change of Product Restriction'),
			('Others - Update Cost Center', 'Others - Update Cost Center'),
		)
		restrictions= (
			('S: Super Only', 'S: Super Only'),
			('U: Super Unleaded Only', 'U: Super Unleaded Only'),
			('R: Regular Only', 'R: Regular Only'),
			('X: Velocity', 'X: Velocity'),
			('D: Diesoline Only', 'D: Diesoline Only'),
			('L: Lubricant Only', 'L: Lubricant Only'),
			('V: Service Only', 'V: Service Only'),
			('C: Convenience store items, sundries, accesories', 'C: Convenience store items, sundries, accesories'),
		)
		approved= (
			('Ser Roy Perluval Dela Cruz','Ser Roy Perluval Dela Cruz'),
		)
		cancellation= (
			('Disposal Of Vehicle','Disposal Of Vehicle'),
			('Resignation of User','Resignation of User'),
		)
		widgets = {
			'date_received': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'application_type': forms.Select(attrs={'class':'form-control', 'choices':'app_type'}),
			'fleet_provider': forms.Select(attrs={'class':'form-control', 'choices':'fleet_card'}),
			'fleetcard_type': forms.Select(attrs={'class':'form-control', 'choices':'card_type'}),
			'fuel_limit_amount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
			'fuel_limit_quantity': forms.TextInput(attrs={'class':'form-control','type':'number'}),
			'products_restriction': forms.Select(attrs={'class':'form-control','choices':'restrictions'}),
			'req_employee_id': forms.TextInput(attrs={'class':'form-control'}),
			'req_fname': forms.TextInput(attrs={'class':'form-control'}),
			'req_lname': forms.TextInput(attrs={'class':'form-control'}),
			'req_title': forms.TextInput(attrs={'class':'form-control'}),
			'req_cost_center': forms.TextInput(attrs={'class':'form-control','type':'number'}),
			'atd_no': forms.TextInput(attrs={'class':'form-control'}),
			'temporary_atd': forms.TextInput(attrs={'class':'form-control'}),
			'new_emp_id': forms.TextInput(attrs={'class':'form-control'}),
			'new_emp_fname': forms.TextInput(attrs={'class':'form-control'}),
			'new_emp_lname': forms.TextInput(attrs={'class':'form-control'}),
			'new_emp_cost': forms.TextInput(attrs={'class':'form-control'}),
			'new_temp_atd': forms.TextInput(attrs={'class':'form-control'}),
			'new_assignee': forms.TextInput(attrs={'class':'form-control'}),
			'cost_center_code': forms.TextInput(attrs={'class':'form-control','type':'number'}),
			'cancellation': forms.Select(attrs={'class':'form-control', 'choices':'cancellation'}),
			'plate_no': forms.TextInput(attrs={'class':'form-control'}),
			'con_sticker': forms.TextInput(attrs={'class':'form-control'}),
			'model_year': forms.TextInput(attrs={'class':'form-control','type':'number'}),
			'brand': forms.TextInput(attrs={'class':'form-control'}),
			'make': forms.TextInput(attrs={'class':'form-control'}),
			'fuel_type': forms.TextInput(attrs={'class':'form-control'}),
			'new_plate_no': forms.TextInput(attrs={'class':'form-control'}),
			'new_cond_sticker': forms.TextInput(attrs={'class':'form-control'}),
			'new_model_year': forms.TextInput(attrs={'class':'form-control','type':'number'}),
			'new_vbrand': forms.TextInput(attrs={'class':'form-control'}),
			'new_vmake': forms.TextInput(attrs={'class':'form-control'}),
			'new_vfuel_type': forms.TextInput(attrs={'class':'form-control'}),
			'approved_by' : forms.Select(attrs={'class':'form-control','choices':'approved'}),
			'date_summitted': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'fleet_received': forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'fleet_card_no': forms.TextInput(attrs={'class':'form-control'}),
			'fleet_date_release' : forms.TextInput(attrs={'class':'form-control','type':'date'}),
			'person_release' : forms.TextInput(attrs={'class':'form-control'}),
			'GCR_SLA': forms.TextInput(attrs={'class':'form-control','value':'10','hidden':'True'})
		}







