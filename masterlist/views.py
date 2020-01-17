from django.shortcuts import render,HttpResponseRedirect,HttpResponse,reverse
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

# def vlistmaster(request):
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#     return render(request, 'vehicleMasterlist/vmasterlist.html')


class VmasterlistCreateView(CreateView):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    model = VehicleMasterList
    form_class = Vmasterlist
    template_name = 'vehicleMasterlist/vehicleMasterlist_form.html'

    def ending(self, request, *args, **kwargs):
        v_id = self.request.POST.get('Activity_Id')

        if request.method == 'POST':
            plate = request.POST.get('PLATE_NO')
            # def getSumOfLastDigits(plate): 
            #     ending = 0 
            #     for num in plate:
            #         ending += num % 10
            #     return ending
            def increment(string):
                plate = int(string[:-1])
                plate += 1
                return string[:-1]
            saveto_end = VehicleMasterList(PLATE_ENDING=ending)
            saveto_end.save()

        return super().post(request)

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

class vehicleMasterDetails(DetailView):
    # def dispatch(self, *args, **kwargs):
    #      return super().dispatch(*args, **kwargs)
    model = VehicleMasterList
    template_name = 'vehicleMasterlist/vehicleMasterlist_details.html'

    # def get_context_data(self, **kwargs):
    #      context = super().get_context_data(**kwargs)
    #      context['VML'] = VehicleMasterList.objects.filter(Activity_id=self.object.pk)
    #      return context

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
    reg1 = VehicleMasterList.objects.filter(PLATE_NO__endswith="1")
    reg2 = VehicleMasterList.objects.filter(PLATE_NO__endswith="2")
    reg3 = VehicleMasterList.objects.filter(PLATE_NO__endswith="3")
    reg4 = VehicleMasterList.objects.filter(PLATE_NO__endswith="4")
    reg5 = VehicleMasterList.objects.filter(PLATE_NO__endswith="5")
    reg6 = VehicleMasterList.objects.filter(PLATE_NO__endswith="6")
    reg7 = VehicleMasterList.objects.filter(PLATE_NO__endswith="7")
    reg8 = VehicleMasterList.objects.filter(PLATE_NO__endswith="8")
    reg9 = VehicleMasterList.objects.filter(PLATE_NO__endswith="9")
    reg0 = VehicleMasterList.objects.filter(PLATE_NO__endswith="0")
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
            'NO',
            'PLATE_NO',
            'CS_NO',
            'CR_NAME',
            'PLATE_ENDING',
            'MODEL',
            'BRAND',
            'VEHICLE_MAKE',
            'ENGINE_NO',
            'CHASSIS_NO',
            'MV_FILE_NO',
            'VEHICLE_TYPE',
            'VEHICLE_CATEGORY',
            'Employee_Id',
            'BAND_LEVEL',
            'BENEFIT_GROUP',
            'COST_CENTER',
            'GROUP',
            'DIVISION',
            'DEPARTMENT',
            'SECTION',
            'IS_ID',
            'IS_FIRST_NAME',
            'IS_LAST_NAME',
            'LOCATION',
            'ACQ_DATE',
            'ACQ_COST',
            'ASSET_NO',
            'PO_NO',
            'EQUIPMENT_NO',
            'ASSIGNEE_LAST_NAME',
            'ASSIGNEE_FIRST_NAME',
            'REGISTRATION_MONTH',
            'ORIGINAL_OR_DATE',
            'PLATE_NUMBER_RELEASE_DATE',
    ]
    row_num = 1

    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title

    for vehicle in v_queryset:
        row_num += 1
        # ordate = vehicle.ORIGINAL_OR_DATE.strftime('%m/%d/%Y')
        # platerelease = vehicle.PLATE_NUMBER_RELEASE_DATE.strftime('%m/%d/%Y')
        row = [
                vehicle.NO,
                vehicle.PLATE_NO,
                vehicle.CS_NO,
                vehicle.CR_NAME,
                vehicle.PLATE_ENDING,
                vehicle.MODEL,
                vehicle.BRAND,
                vehicle.VEHICLE_MAKE,
                vehicle.ENGINE_NO,
                vehicle.CHASSIS_NO,
                vehicle.MV_FILE_NO,
                vehicle.VEHICLE_TYPE,
                vehicle.VEHICLE_CATEGORY,
                vehicle.Employee_Id,
                vehicle.BAND_LEVEL,
                vehicle.BENEFIT_GROUP,
                vehicle.COST_CENTER,
                vehicle.GROUP,
                vehicle.DIVISION,
                vehicle.DEPARTMENT,
                vehicle.SECTION,
                vehicle.IS_ID,
                vehicle.IS_FIRST_NAME,
                vehicle.IS_LAST_NAME,
                vehicle.LOCATION,
                vehicle.ACQ_DATE,
                vehicle.ACQ_COST,
                vehicle.ASSET_NO,
                vehicle.PO_NO,
                vehicle.EQUIPMENT_NO,
                vehicle.ASSIGNEE_LAST_NAME,
                vehicle.ASSIGNEE_FIRST_NAME,
                vehicle.REGISTRATION_MONTH,
                vehicle.ORIGINAL_OR_DATE,
                vehicle.PLATE_NUMBER_RELEASE_DATE,
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





