from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import EmployeeMasterlist,VehicleMasterList




class EmpMasterlistForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(EmpMasterlistForm, self).__init__(*args, **kwargs)
            self.fields['Suffix'].required = False
            self.fields['External_role'].required = False
            self.fields['Unit'].required = False
            self.fields['Sub_unit'].required = False
            
      class Meta:
            model = EmployeeMasterlist
            fields = [
                  'Company','Employee_Id','Last_name','First_name','Middle_name','Suffix','External_role',
                  'Job_category','Hiring_date','Tenure','Band','Cost_center','DIV_code','Group','Division',
                  'Department','Section','Unit','Sub_unit','IS_ID','IS_lastname','IS_firstname','Location',
                  'Area','Area2','Benefit'
            ]
            widgets = {
                  'Company': forms.TextInput(attrs={'class':'form-control'}),
                  'Employee_Id':forms.TextInput(attrs={'class':'form-control'}),
                  'Last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'First_name':forms.TextInput(attrs={'class':'form-control'}),
                  'Middle_name':forms.TextInput(attrs={'class':'form-control'}),
                  'Suffix':forms.TextInput(attrs={'class':'form-control'}),
                  'External_role':forms.TextInput(attrs={'class':'form-control'}),
                  'Job_category':forms.TextInput(attrs={'class':'form-control'}),
                  'Hiring_date':forms.TextInput(attrs={'class':'form-control','type':'date'}),
                  'Tenure':forms.TextInput(attrs={'class':'form-control'}),
                  'Band':forms.TextInput(attrs={'class':'form-control'}),
                  'Cost_center':forms.TextInput(attrs={'class':'form-control','type':'number'}),
                  'DIV_code':forms.TextInput(attrs={'class':'form-control'}),
                  'Group':forms.TextInput(attrs={'class':'form-control'}),
                  'Division':forms.TextInput(attrs={'class':'form-control'}),
                  'Department':forms.TextInput(attrs={'class':'form-control'}),
                  'Section':forms.TextInput(attrs={'class':'form-control'}),
                  'Unit':forms.TextInput(attrs={'class':'form-control'}),
                  'Sub_unit':forms.TextInput(attrs={'class':'form-control'}),
                  'IS_ID':forms.TextInput(attrs={'class':'form-control'}),
                  'IS_lastname':forms.TextInput(attrs={'class':'form-control'}),
                  'IS_firstname':forms.TextInput(attrs={'class':'form-control'}),
                  'Location':forms.TextInput(attrs={'class':'form-control'}),
                  'Area':forms.TextInput(attrs={'class':'form-control'}),
                  'Area2':forms.TextInput(attrs={'class':'form-control'}),
                  'Benefit':forms.TextInput(attrs={'class':'form-control'})
            }

class Vmasterlist(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(Vmasterlist, self).__init__(*args, **kwargs)
            self.fields['PLATE_NO'].required = False
            self.fields['CS_NO'].required = False
            self.fields['PLATE_ENDING'].required = False
            self.fields['REGISTRATION_MONTH'].required = False
            self.fields['MODEL'].required = False
            self.fields['BRAND'].required = False
            self.fields['VEHICLE_MAKE'].required = False
            self.fields['ENGINE_NO'].required = False
            self.fields['CHASSIS_NO'].required = False
            self.fields['MV_FILE_NO'].required = False
            self.fields['VEHICLE_TYPE'].required = False
            self.fields['ASSIGNEE_LAST_NAME'].required = False
            self.fields['ASSIGNEE_FIRST_NAME'].required = False
            self.fields['VEHICLE_CATEGORY'].required = False
            self.fields['Employee_Id'].required = False
            self.fields['BAND_LEVEL'].required = False
            self.fields['BENEFIT_GROUP'].required = False
            self.fields['COST_CENTER'].required = False
            self.fields['GROUP'].required = False
            self.fields['DIVISION'].required = False
            self.fields['DEPARTMENT'].required = False
            self.fields['SECTION'].required = False
            self.fields['IS_ID'].required = False
            self.fields['IS_LAST_NAME'].required = False
            self.fields['IS_FIRST_NAME'].required = False
            self.fields['LOCATION'].required = False
            self.fields['ORIGINAL_OR_DATE'].required = False
            self.fields['ACQ_DATE'].required = False
            self.fields['ACQ_COST'].required = False
            self.fields['ASSET_NO'].required = False
            self.fields['EQUIPMENT_NO'].required = False
            self.fields['PO_NO'].required = False
            self.fields['PLATE_NUMBER_RELEASE_DATE'].required = False

      class Meta:
            model = VehicleMasterList
            fields = [
                  'PLATE_NO','CS_NO','CR_NAME','PLATE_ENDING','REGISTRATION_MONTH','MODEL','BRAND',
                  'VEHICLE_MAKE','ENGINE_NO','CHASSIS_NO','MV_FILE_NO','VEHICLE_TYPE','ASSIGNEE_LAST_NAME','ASSIGNEE_FIRST_NAME','VEHICLE_CATEGORY','Employee_Id',
                  'BAND_LEVEL','BENEFIT_GROUP','COST_CENTER','GROUP','DIVISION','DEPARTMENT','SECTION','IS_ID','IS_LAST_NAME','IS_FIRST_NAME','LOCATION','ORIGINAL_OR_DATE',
                  'ACQ_DATE','ACQ_COST','ASSET_NO','EQUIPMENT_NO','PO_NO','PLATE_NUMBER_RELEASE_DATE'
            ]

            Vbrand= (
                  ('Honda','Honda'),
                  ('Toyota','Toyota'),
                  ('Mitsubishi','Mitsubishi'),
                  ('Ford','Ford'),
                  ('Masda','Masda'),
                  ('Isuzu','Isuzu'),
                  ('Hyundai','Hyundai'),
                  ('Nissan','Nissan'),
                  ('SuZuki','Suzuki'),
                  ('Chevrolet','Chevrolet'),
            )

            widgets = {
                  'PLATE_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CS_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CR_NAME': forms.TextInput(attrs={'class':'form-control'}),
                  'PLATE_ENDING': forms.TextInput(attrs={'class':'form-control'}),
                  'REGISTRATION_MONTH': forms.TextInput(attrs={'class':'form-control'}),
                  'MODEL': forms.TextInput(attrs={'class':'form-control'}),
                  'BRAND': forms.Select(attrs={'class':'form-control','choices':'Vbrand'}),
                  'VEHICLE_MAKE': forms.TextInput(attrs={'class':'form-control'}),
                  'ENGINE_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CHASSIS_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'MV_FILE_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'VEHICLE_TYPE': forms.TextInput(attrs={'class':'form-control'}),
                  'ASSIGNEE_LAST_NAME': forms.TextInput(attrs={'class':'form-control'}),
                  'ASSIGNEE_FIRST_NAME': forms.TextInput(attrs={'class':'form-control'}),
                  'VEHICLE_CATEGORY': forms.TextInput(attrs={'class':'form-control'}),
                  'Employee_Id' : forms.Select(attrs={'class':'form-control'}),
                  'BAND_LEVEL' : forms.TextInput(attrs={'class':'form-control'}),
                  'BENEFIT_GROUP': forms.TextInput(attrs={'class':'form-control'}),
                  'COST_CENTER': forms.TextInput(attrs={'class':'form-control'}),
                  'GROUP': forms.TextInput(attrs={'class':'form-control'}),
                  'DIVISION': forms.TextInput(attrs={'class':'form-control'}),
                  'DEPARTMENT': forms.TextInput(attrs={'class':'form-control'}),
                  'SECTION': forms.TextInput(attrs={'class':'form-control'}),
                  'IS_ID': forms.TextInput(attrs={'class':'form-control'}),
                  'IS_LAST_NAME': forms.TextInput(attrs={'class':'form-control'}),
                  'IS_FIRST_NAME': forms.TextInput(attrs={'class':'form-control'}),
                  'LOCATION': forms.TextInput(attrs={'class':'form-control'}),
                  'ORIGINAL_OR_DATE' : forms.TextInput(attrs={'class':'form-control', 'hidden':'true'}),
                  'ACQ_DATE': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
                  'ACQ_COST': forms.TextInput(attrs={'class':'form-control'}),
                  'ASSET_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'EQUIPMENT_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'PO_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'PLATE_NUMBER_RELEASE_DATE': forms.TextInput(attrs={'class':'form-control'})

                  # 'Plate_no': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Conduction_Sticker': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Remarks': forms.TextInput(attrs={'class':'form-control'}),
                  # 'CR_name': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Ending': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Model': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Brand': forms.Select(attrs={'class':'form-control','choices':'Vbrand'}),
                  # 'Vehicle_make': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Engine_No': forms.TextInput(attrs={'class':'form-control'}),
                  # 'MV_file_no': forms.TextInput(attrs={'class':'form-control'}),
                  # 'vehicle_type': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Vehicle_category': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Employee_Id': forms.Select(attrs={'class':'form-control'}),
                  # 'Band_level': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Band_Benefit': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Contact_no': forms.TextInput(attrs={'class':'form-control','type':'number'}),
                  # 'Cost_center': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Group': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Division': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Department': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Section': forms.TextInput(attrs={'class':'form-control'}),
                  # 'IS_employee_ID': forms.TextInput(attrs={'class':'form-control'}),
                  # 'IS_firstname': forms.TextInput(attrs={'class':'form-control'}),
                  # 'IS_lastname': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Location': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Aquisition_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
                  # 'Aquisition_cost': forms.TextInput(attrs={'class':'form-control','type':'number'}),
                  # 'Asset_no': forms.TextInput(attrs={'class':'form-control'}),
                  # 'PO_no': forms.TextInput(attrs={'class':'form-control'}),
                  # 'SAP_PR': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Vehicle_IVN_no': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Unit_MATDOC': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Grdd_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
                  # 'Equipment_no': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Latest_registration': forms.TextInput(attrs={'class':'form-control','type':'date'}),
                  # 'Lates_remark': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Lname_assignee': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Fname_assignee': forms.TextInput(attrs={'class':'form-control'}),
                  # 'reg_month': forms.TextInput(attrs={'class':'form-control', 'hidden':'true'}),
                  # 'original_OR_date': forms.TextInput(attrs={'class':'form-control', 'hidden':'true'}),
                  # 'plateNo_release': forms.TextInput(attrs={'class':'form-control', 'hidden':'true'})
            }

class Vmaster(forms.ModelForm):
      def __init__(self, *args, **kwargs):
            super(Vmaster, self).__init__(*args, **kwargs)
            self.fields['original_OR_date'].required = False
            
      class Meta:
            model = VehicleMasterList
            exclude = ('ENGINE_NO','CHASSIS_NO','MV_FILE_NO','VEHICLE_TYPE','ASSIGNEE_LAST_NAME','ASSIGNEE_FIRST_NAME','VEHICLE_CATEGORY','Employee_Id',
                  'BAND_LEVEL','BENEFIT_GROUP','COST_CENTER','GROUP','DIVISION','DEPARTMENT','SECTION','IS_ID','IS_LAST_NAME','IS_FIRST_NAME','LOCATION',
                  'ACQ_DATE','ACQ_COST','ASSET_NO','EQUIPMENT_NO','PO_NO',
                  )
            fields = [
                  'PLATE_NO','CS_NO','CR_NAME','PLATE_ENDING','REGISTRATION_MONTH','MODEL','BRAND',
                  'VEHICLE_MAKE','ORIGINAL_OR_DATE','ENGINE_NO','CHASSIS_NO','MV_FILE_NO','VEHICLE_TYPE','ASSIGNEE_LAST_NAME','ASSIGNEE_FIRST_NAME','VEHICLE_CATEGORY','Employee_Id',
                  'BAND_LEVEL','BENEFIT_GROUP','COST_CENTER','GROUP','DIVISION','DEPARTMENT','SECTION','IS_ID','IS_LAST_NAME','IS_FIRST_NAME','LOCATION',
                  'ACQ_DATE','ACQ_COST','ASSET_NO','EQUIPMENT_NO','PO_NO','PLATE_NUMBER_RELEASE_DATE'

            ]

            widgets = {
                  # 'PLATE_NO': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  # 'Conduction_Sticker': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  # 'Remarks': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  # 'CR_name': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  # 'Ending': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  # 'Model': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  # 'Brand': forms.Select(attrs={'class':'form-control','readonly':'true'}),
                  # 'Vehicle_make': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  # 'Engine_No': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  # 'MV_file_no': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  # 'vehicle_type': forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
                  # 'original_OR_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
                  # 'plateNo_release': forms.TextInput(attrs={'class':'form-control','type':'date'})

                  'PLATE_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CS_NO': forms.TextInput(attrs={'class':'form-control'}),
                  'CR_NAME': forms.TextInput(attrs={'class':'form-control'}),
                  'PLATE_ENDING': forms.TextInput(attrs={'class':'form-control'}),
                  'REGISTRATION_MONTH': forms.TextInput(attrs={'class':'form-control'}),
                  'MODEL': forms.TextInput(attrs={'class':'form-control'}),
                  'BRAND': forms.Select(attrs={'class':'form-control','choices':'Vbrand'}),
                  'VEHICLE_MAKE': forms.TextInput(attrs={'class':'form-control'}),
                  'ORIGINAL_OR_DATE' : forms.TextInput(attrs={'class':'form-control', 'hidden':'true'}),
                  'PLATE_NUMBER_RELEASE_DATE': forms.TextInput(attrs={'class':'form-control', 'hidden':'true'})
            }


