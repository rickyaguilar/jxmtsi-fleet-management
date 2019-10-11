from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import VehicleMasterList




class vehiclemasterlist(forms.Form):
    class Meta:
        model = VehicleMasterList
            Plate_no = forms.CharField()
            Conduction_Sticker = forms.CharField()
            Remarks = forms.CharField()
            CR_name = forms.CharField()
            Ending = forms.CharField()
            Model = forms.CharField()
            Brand = forms.CharField()
            Vehicle_make = forms.CharField()
            Engine_No = forms.CharField()
            Chassis_no = forms.CharField()
            MV_file_no = forms.CharField()
            vehicle_type = forms.CharField()
            Last_name_assignee = forms.CharField()
            First_name_assignee = forms.CharField()
            Vehicle_category = forms.CharField()
            Employee_Id = forms.CharField()
            Band_level = forms.CharField()
            Band_Benefit = forms.CharField()
            Contact_no = forms.CharField()
            Cost_center = forms.CharField()
            Group = forms.CharField()
            Division = forms.CharField()
            Department =forms.CharField()
            Section = forms.CharField()
            IS_employee_ID =forms.CharField()
            IS_firstname=forms.CharField()
            IS_lastname =forms.CharField()
            Location = forms.CharField()
            Aquisition_date = forms.DateField()
            Aquisition_cost = forms.CharField()
            Asset_no = forms.CharField()
            PO_no = forms.CharField()
            SAP_PR = forms.CharField()
            Vehicle_IVN_no = forms.CharField()
            Unit_MATDOC = forms.CharField()
            Grdd_date = forms.CharField()
            Equipment_no =forms.CharField()
            Latest_registration =forms.CharField()
            Lates_remark=forms.CharField()
            Sold_vehicle=forms.CharField()
