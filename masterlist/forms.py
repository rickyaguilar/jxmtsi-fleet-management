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
            self.fields['SAP_PR'].required = False
            self.fields['Vehicle_IVN_no'].required = False
            self.fields['Unit_MATDOC'].required = False
            self.fields['Grdd_date'].required = False

      class Meta:
            model = VehicleMasterList
            fields = [
                  'Plate_no','Conduction_Sticker','Remarks','CR_name','Ending','Model','Brand','Vehicle_make','Engine_No',
                  'MV_file_no','vehicle_type','Vehicle_category','Employee_Id','Band_level',
                  'Band_Benefit','Contact_no','Cost_center','Group','Division','Department' ,'Section','IS_employee_ID','IS_firstname',
                  'IS_lastname','Location','Aquisition_date','Aquisition_cost','Asset_no','PO_no','SAP_PR','Vehicle_IVN_no',
                  'Unit_MATDOC','Grdd_date','Equipment_no','Latest_registration','Lates_remark','Lname_assignee','Fname_assignee'

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
                  'Plate_no': forms.TextInput(attrs={'class':'form-control'}),
                  'Conduction_Sticker': forms.TextInput(attrs={'class':'form-control'}),
                  'Remarks': forms.TextInput(attrs={'class':'form-control'}),
                  'CR_name': forms.TextInput(attrs={'class':'form-control'}),
                  'Ending': forms.TextInput(attrs={'class':'form-control'}),
                  # 'Model': forms.TextInput(attrs={'class':'form-control'}),
                  'Brand': forms.Select(attrs={'class':'form-control','choices':'Vbrand'}),
                  'Brand': forms.TextInput(attrs={'class':'form-control'}),
                  'Vehicle_make': forms.TextInput(attrs={'class':'form-control'}),
                  'Engine_No': forms.TextInput(attrs={'class':'form-control'}),
                  'MV_file_no': forms.TextInput(attrs={'class':'form-control'}),
                  'vehicle_type': forms.TextInput(attrs={'class':'form-control'}),
                  'Vehicle_category': forms.TextInput(attrs={'class':'form-control'}),
                  'Employee_Id': forms.TextInput(attrs={'class':'form-control'}),
                  'Band_level': forms.TextInput(attrs={'class':'form-control'}),
                  'Band_Benefit': forms.TextInput(attrs={'class':'form-control'}),
                  'Contact_no': forms.TextInput(attrs={'class':'form-control','type':'number'}),
                  'Cost_center': forms.TextInput(attrs={'class':'form-control'}),
                  'Group': forms.TextInput(attrs={'class':'form-control'}),
                  'Division': forms.TextInput(attrs={'class':'form-control'}),
                  'Department': forms.TextInput(attrs={'class':'form-control'}),
                  'Section': forms.TextInput(attrs={'class':'form-control'}),
                  'IS_employee_ID': forms.TextInput(attrs={'class':'form-control'}),
                  'IS_firstname': forms.TextInput(attrs={'class':'form-control'}),
                  'IS_lastname': forms.TextInput(attrs={'class':'form-control'}),
                  'Location': forms.TextInput(attrs={'class':'form-control'}),
                  'Aquisition_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
                  'Aquisition_cost': forms.TextInput(attrs={'class':'form-control','type':'number'}),
                  'Asset_no': forms.TextInput(attrs={'class':'form-control'}),
                  'PO_no': forms.TextInput(attrs={'class':'form-control'}),
                  'SAP_PR': forms.TextInput(attrs={'class':'form-control'}),
                  'Vehicle_IVN_no': forms.TextInput(attrs={'class':'form-control'}),
                  'Unit_MATDOC': forms.TextInput(attrs={'class':'form-control'}),
                  'Grdd_date': forms.TextInput(attrs={'class':'form-control','type':'date'}),
                  'Equipment_no': forms.TextInput(attrs={'class':'form-control'}),
                  'Latest_registration': forms.TextInput(attrs={'class':'form-control','type':'date'}),
                  'Lates_remark': forms.TextInput(attrs={'class':'form-control'}),
                  'Lname_assignee': forms.TextInput(attrs={'class':'form-control'}),
                  'Fname_assignee': forms.TextInput(attrs={'class':'form-control'})
            }



