from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from openpyxl import Workbook
from django.urls import reverse_lazy
from django.views import generic
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
     ListView,
     CreateView,
     DetailView,
     UpdateView,
 )
from .models import (
	EmployeeMasterlist,
	VehicleMasterList
	)

from . forms import (
	EmpMasterlistForm,
	Vmasterlist,
    Vmaster
	)
from bootstrap_modal_forms.generic import (
                                           BSModalDeleteView
                                           )

class VmasterlistCreateView(CreateView):
	model = VehicleMasterList
	form_class = Vmasterlist
	template_name = 'vehicleMasterlist/vehicleMasterlist_form.html'

    # def post(self, request):
    #     plate = VehicleMasterList.objects.Filter('Plate_no')
    #     if  plate == '0':
    #         reg = "Oct"
    #         save_to_vechile = VehicleMasterList(reg_month=reg)
    #     else if plate =='1'
    #         reg1 = "Jan"
    #         save_to_vechile = VehicleMasterList(reg_month=reg1)
    #     else if plate =='2'
    #         reg2 = "Feb"
    #         save_to_vechile = VehicleMasterList(reg_month=reg2)
    #     else if plate =='3'
    #         reg3 = "March"
    #         save_to_vechile = VehicleMasterList(reg_month=reg3)
    #     else if plate =='4'
    #         reg4 = "April"
    #         save_to_vechile = VehicleMasterList(reg_month=reg4)
    #     else if plate =='5'
    #         reg5 = "May"
    #         save_to_vechile = VehicleMasterList(reg_month=reg5)
    #     else if plate =='6'
    #         reg6 = "June"
    #         save_to_vechile = VehicleMasterList(reg_month=reg6)
    #     else if plate =='7'
    #         reg7 = "July"
    #         save_to_vechile = VehicleMasterList(reg_month=reg7)
    #     else if plate =='8'
    #         reg8 = "Aug"
    #         save_to_vechile = VehicleMasterList(reg_month=reg8)
    #     else
    #         reg9 = "Sept"
    #         save_to_vechile = VehicleMasterList(reg_month=reg9)


    #     return super().post(request)
# def Vmaster(request):
#     vlist = VehicleMasterList.objects.all()
#     return render(request, 'registration/release_date.html', {'title': 'Registration - Update Registration', 'vlist': vlist})

# def vmaster_update(request, pk):
#     if request.method == 'POST':
#         plate_release = request.POST.get('plate_release')

#         VehicleMasterList.objects.filter(id=pk).update(plateNo_release=plate_release)
#         return HttpResponseRedirect('/Masterlist/VehicleMasterlist/')

class vehicleMasterListView(ListView):
	model = VehicleMasterList
	template_name = 'vehicleMasterlist/vehicleMasterlist.html'

# class vehicleMasterDetails(DetailView):
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#     model = VehicleMasterList
#     template_name = 'vehicleMasterlist/vehicleMasterlist_details.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['VML'] = VehicleMasterList.objects.filter(Activity_id=self.object.pk)
#         return context

class vehicleMasterUpdate(UpdateView):
	model = VehicleMasterList
	form_class = Vmasterlist
	template_name = 'vehicleMasterlist/vehicleMasterlist_form.html'

class releaseUpdate(UpdateView):
    model = VehicleMasterList
    form_class = Vmaster
    template_name = 'registration/release_date.html'

class vehicleMasterlistDeleteView(BSModalDeleteView):
    model = VehicleMasterList
    template_name = 'vehicleMasterlist/vehicleMasterlist_delete.html'
    success_message = 'Success: Item was deleted.'
    success_url = reverse_lazy('vehicle-list')

class employeeCreateView(CreateView):
    model = EmployeeMasterlist
    form_class = EmpMasterlistForm
    template_name = 'employeeMasterlist/employeeMasterlist_form.html'

class employeeListView(ListView):
	model = EmployeeMasterlist
	template_name = 'employeeMasterlist/employeeMasterlist.html'

class employeeDetailView(DetailView):
	model = EmployeeMasterlist
	template_name = 'employeeMasterlist/employeeMasterlist_details.html'

class employeeUpdateView(UpdateView):
    model = EmployeeMasterlist
    form_class = EmpMasterlistForm
    template_name = 'employeeMasterlist/employeeMasterlist_form.html'

class employeeMasterlistDeleteView(BSModalDeleteView):
    model = EmployeeMasterlist
    template_name = 'employeeMasterlist/employeeMasterlist_delete.html'
    success_message = 'Success: Item was deleted.'
    success_url = reverse_lazy('employee-list')


def registration(request):
    model = VehicleMasterList
    reg1 = VehicleMasterList.objects.filter(Plate_no__endswith="1")
    reg2 = VehicleMasterList.objects.filter(Plate_no__endswith="2")
    reg3 = VehicleMasterList.objects.filter(Plate_no__endswith="3")
    reg4 = VehicleMasterList.objects.filter(Plate_no__endswith="4")
    reg5 = VehicleMasterList.objects.filter(Plate_no__endswith="5")
    reg6 = VehicleMasterList.objects.filter(Plate_no__endswith="6")
    reg7 = VehicleMasterList.objects.filter(Plate_no__endswith="7")
    reg8 = VehicleMasterList.objects.filter(Plate_no__endswith="8")
    reg9 = VehicleMasterList.objects.filter(Plate_no__endswith="9")
    reg0 = VehicleMasterList.objects.filter(Plate_no__endswith="0")
    return render(request, 'registration/registration.html', {'title': 'Vehicle - Vehicle Filter', 'reg1': reg1,'reg2': reg2, 'reg3': reg3,
    'reg4': reg4, 'reg5': reg5, 'reg6': reg6, 'reg7': reg7, 'reg8': reg8, 'reg9': reg9, 'reg0': reg0})

def vehicle_excel(request):
    v_queryset = VehicleMasterList.objects.all()   
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=Vehicle Masterlist.xlsx'
    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = 'Vehicle Masterlist'

    columns = [
            'No',
            'Plate_no',
            'Conduction_Sticker',
            'Remarks',
            'CR_name',
            'Ending',
            'Model',
            'Brand',
            'Vehicle_make',
            'Engine_No',
            'Chassis_no',
            'MV_file_no',
            'vehicle_type',
            'Vehicle_category',
            'Employee_Id',
            'Band_level',
            'Band_Benefit',
            'Contact_no',
            'Cost_center',
            'Group',
            'Division',
            'Department',
            'Section',
            'IS_employee_ID',
            'IS_firstname',
            'IS_lastname',
            'Location',
            'Aquisition_date',
            'Aquisition_cost',
            'Asset_no',
            'PO_no',
            'SAP_PR',
            'Vehicle_IVN_no',
            'Unit_MATDOC',
            'Grdd_date',
            'Equipment_no',
            'Latest_registration',
            'Lates_remark',
            'Lname_assignee',
            'Fname_assignee',
            'reg_month',
            'original_OR_date',
            'plateNo_release',
    ]
    row_num = 1

    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    for vehicle in v_queryset:
        row_num += 1
        ordate = vehicle.original_OR_date.strftime('%m/%d/%Y')
        platerelease = vehicle.plateNo_release.strftime('%m/%d/%Y')
        row = [
                vehicle.No,
                vehicle.Plate_no,
                vehicle.Conduction_Sticker,
                vehicle.Remarks,
                vehicle.CR_name,
                vehicle.Ending,
                vehicle.Model,
                vehicle.Brand,
                vehicle.Vehicle_make,
                vehicle.Engine_No,
                vehicle.Chassis_no,
                vehicle.MV_file_no,
                vehicle.vehicle_type,
                vehicle.Vehicle_category,
                vehicle.Employee_Id,
                vehicle.Band_level,
                vehicle.Band_Benefit,
                vehicle.Contact_no,
                vehicle.Cost_center,
                vehicle.Group,
                vehicle.Division,
                vehicle.Department,
                vehicle.Section,
                vehicle.IS_employee_ID,
                vehicle.IS_firstname,
                vehicle.IS_lastname,
                vehicle.Location,
                vehicle.Aquisition_date,
                vehicle.Aquisition_cost,
                vehicle.Asset_no,
                vehicle.PO_no,
                vehicle.SAP_PR,
                vehicle.Vehicle_IVN_no,
                vehicle.Unit_MATDOC,
                vehicle.Grdd_date,
                vehicle.Equipment_no,
                vehicle.Latest_registration,
                vehicle.Lates_remark,
                vehicle.Lname_assignee,
                vehicle.Fname_assignee,
                vehicle.reg_month,
                ordate,
                platerelease,
        ]
        
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value

    workbook.save(response)
    return response

def employee_excel(request):
    emp_queryset = EmployeeMasterlist.objects.all()   
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename=Employee Masterlist.xlsx'
    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = 'Employee Masterlist'

    columns = [
            'Company',
            'Employee_Id',
            'Last_name',
            'First_name',
            'Middle_name',
            'Suffix',
            'External_role',
            'Job_category',
            'Hiring_date',
            'Tenure',
            'Band',
            'Cost_center',
            'DIV_code',
            'Group',
            'Division',
            'Department',
            'Section',
            'Unit',
            'Sub_unit',
            'IS_ID',
            'IS_lastname',
            'IS_firstname',
            'Location',
            'Area',
            'Area2',
            'Benefit',
    ]
    row_num = 1

    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    for emp in emp_queryset:
        row_num += 1

        row = [
            emp.Company,
            emp.Employee_Id,
            emp.Last_name,
            emp.First_name,
            emp.Middle_name,
            emp.Suffix,
            emp.External_role,
            emp.Job_category,
            emp.Hiring_date,
            emp.Tenure,
            emp.Band,
            emp.Cost_center,
            emp.DIV_code,
            emp.Group,
            emp.Division,
            emp.Department,
            emp.Section,
            emp.Unit,
            emp.Sub_unit,
            emp.IS_ID,
            emp.IS_lastname,
            emp.IS_firstname,
            emp.Location,
            emp.Area,
            emp.Area2,
            emp.Benefit,
        ]
        
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value

    workbook.save(response)
    return response





