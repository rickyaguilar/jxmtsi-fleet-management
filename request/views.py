from django.views import generic
from django.shortcuts import render,HttpResponseRedirect, get_list_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import (
		CarRentalRequest,
        Gas_card,
        service_vehicle,
        Vehicle_Repair,
)
from masterlist.models import EmployeeMasterlist,VehicleMasterList
from django.views.generic import (
     DetailView,
     ListView,
     CreateView,
     UpdateView,
 )
# from django.views.generic.edit import (
    # DeleteView,
# )
from . forms import (
    carrequestform,
    gascardform,
    serviceform,
    repairform,

    )

from bootstrap_modal_forms.generic import (
                                           BSModalDeleteView
                                           )


                      #####################################  
                    #########################################
                   #####.       Car Rental Request       #####
                    #########################################
                     ######################################


# class requestCreateView(SuccessMessageMixin, CreateView):
#     model = CarRentalRequest
#     form_class = carrequestform
#     template_name = 'car_rental/carrequest_form.html'

#     def get_success_message(self, cleaned_data):
#     	print(cleaned_data)
#     	return "New Car Rental Request Has been Created!"
def requestCreate(request):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    emplist = EmployeeMasterlist.objects.all()
    return render(request, 'car_rental/carrequest_new.html',{'Title':'Car - Car Request', 'emplist':emplist})
    # def get_success_message(self, cleaned_data):
    #    print(cleaned_data)
    #    return "New Car Rental Request Has been Created!"
def requestsubmit(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        date_received = request.POST.get('date_received')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        cnumber = request.POST.get('cnumber')
        company = request.POST.get('company')
        band = request.POST.get('band')
        dept = request.POST.get('dept')
        cost = request.POST.get('cost')
        div = request.POST.get('div')
        loc = request.POST.get('loc')
        section = request.POST.get('section')
        designation = request.POST.get('designation')
        atd = request.POST.get('atd')
        vname = request.POST.get('vname')
        date = request.POST.get('date')
        up_to = request.POST.get('up_to')
        time = request.POST.get('time')
        del_place = request.POST.get('del_place')
        type_rental = request.POST.get('type_rental')
        costcenter = request.POST.get('costcenter')
        rent_period = request.POST.get('rent_period')
        destination = request.POST.get('destination')
        del_date = request.POST.get('del_date')
        end_user = request.POST.get('end_user')
        vehicle_type = request.POST.get('vehicle_type')
        plate_no = request.POST.get('plate_no')
        supervisor = request.POST.get('supervisor')
        cr_sla = request.POST.get('cr_sla')

        saveto_req = CarRentalRequest(
                A_Employee_Id =emp_id, Date_received = date_received,Assignee_Fname = fname,Assignee_Lname = lname,Assignee_No = cnumber,Assignee_Company = company,
                Assignee_band = band,Assignee_Dept = dept,Assignee_Cost = cost,Assignee_Div = div,Assignee_Loc = loc,Assignee_Section = section,
                Assignee_Designation = designation,Assignee_ATD = atd,Vendor_name = vname,Date = date,Up_to = up_to,Time = time,Place_of_del = del_place,
                type_rental = type_rental,Cost_center = costcenter,Rental_period = rent_period,Destination = destination,Delivery_date = del_date,End_user = end_user,Type_of_vehicle = vehicle_type,
                Plate_no = plate_no,Immediate_supervisor =supervisor ,CR_SLA = cr_sla)
        saveto_req.save()

        return HttpResponseRedirect('/Request/Request/')

class requestListView(ListView):
	model = CarRentalRequest
	template_name = 'car_rental/carrequest_list.html'

class requestDetailView(DetailView):
	model = CarRentalRequest
	template_name = 'car_rental/carrequest_details.html'

class requestUpdateView(SuccessMessageMixin, UpdateView):
    model = CarRentalRequest
    form_class = carrequestform
    template_name = 'car_rental/carrequest_form.html'
    def get_success_message(self, cleaned_data):
    	print(cleaned_data)
    	return "Car Rental Request Updated Successfully!"

# class requestDeleteView(DeleteView):
#     model = CarRentalRequest
#     template_name = 'car_rental/car_delete.html'
#     success_url = reverse_lazy('carrequest_list')

class requestDeleteView(BSModalDeleteView):
    model = CarRentalRequest
    template_name = 'car_rental/car_delete.html'
    success_message = 'Success: Report was deleted.'
    success_url = reverse_lazy('carrequest_list')


                      #####################################  
                    #########################################
                   #####.       Gas Card Request         #####
                    #########################################
                     ######################################


def gascreate(request):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    elist = EmployeeMasterlist.objects.all()
    vlist = VehicleMasterList.objects.all()
    return render(request, 'gas_card/gascard_new.html',{'Title':'Gas - Gas Card Request', 'elist':elist, 'vlist':vlist})
    def get_success_message(self, cleaned_data):
       print(cleaned_data)
       return "New Car Rental Request Has been Created!"

def gassubmit(request):
    if request.method == 'POST':
        date_app = request.POST.get('date_app')
        app_type = request.POST.get('app_type')
        fleet_card = request.POST.get('fleet_card')
        fleet_card_type = request.POST.get('fleet_card_type')
        fuel_amount = request.POST.get('fuel_amount')
        fuel_quantity = request.POST.get('fuel_quantity')
        products_restriction = request.POST.get('products_restriction')
        req_emp_id = request.POST.get('req_emp_id')
        r_fname = request.POST.get('r_fname')
        r_lname = request.POST.get('r_lname')
        r_costcenter = request.POST.get('r_costcenter')
        r_title = request.POST.get('r_title')
        atd_no = request.POST.get('atd_no')
        temp_atd = request.POST.get('temp_atd')
        new_empId = request.POST.get('new_empId')
        new_fname = request.POST.get('new_fname')
        new_lname = request.POST.get('new_lname')
        new_costcenter = request.POST.get('new_costcenter')
        new_tempATD = request.POST.get('new_tempATD')
        new_assignee = request.POST.get('new_assignee')
        cost_code = request.POST.get('cost_code')
        gcr_cancel = request.POST.get('gcr_cancel')
        plate_no = request.POST.get('plate_no')
        c_sticker = request.POST.get('c_sticker')
        gcr_sla = request.POST.get('gcr_sla')
        v_brand = request.POST.get('v_brand')
        v_model = request.POST.get('v_model')
        v_make = request.POST.get('v_make')
        v_fueltype = request.POST.get('v_fueltype')
        new_plate_no = request.POST.get('new_plate_no')
        new_cs = request.POST.get('new_cs')
        new_model = request.POST.get('new_model')
        new_brand = request.POST.get('new_brand')
        new_make = request.POST.get('new_make')
        new_fueltype = request.POST.get('new_fueltype')
        approved_by = request.POST.get('approved_by')
        date_sumitted_app = request.POST.get('date_sumitted_app')
        date_recieved_fleet = request.POST.get('date_recieved_fleet')
        fleet_card_no = request.POST.get('fleet_card_no')
        fleet_card_release = request.POST.get('fleet_card_release')
        person_release_card = request.POST.get('person_release_card')
        gcr_sla = request.POST.get('gcr_sla')

        saveto_gas = Gas_card(date_received = date_app,application_type = app_type,fleet_provider= fleet_card,fleetcard_type =fleet_card_type ,
            fuel_limit_amount = fuel_amount,fuel_limit_quantity = fuel_quantity,products_restriction = products_restriction,req_employee = req_emp_id,
            req_fname = r_fname,req_lname = r_lname ,req_title = r_title,req_cost_center = r_costcenter, atd_no = atd_no,temporary_atd = temp_atd,
            new_emp_id = new_empId,new_emp_fname = new_fname,new_emp_lname =new_lname ,new_emp_cost = new_costcenter,new_temp_atd = new_tempATD,
            new_assignee = new_assignee,cost_center_code = cost_code,cancellation = gcr_cancel,plate_no = plate_no,con_sticker = c_sticker,
            model_year = v_model,brand = v_brand,make = v_make,fuel_type = v_fueltype,new_plate_no = new_plate_no,new_cond_sticker = new_cs,
            new_model_year = new_model,new_vbrand = new_brand,new_vmake = new_make,new_vfuel_type = new_fueltype,approved_by = approved_by,
            date_summitted =date_sumitted_app,fleet_received = date_recieved_fleet,fleet_card_no = fleet_card_no,fleet_date_release = fleet_card_release,
            person_release = person_release_card,GCR_SLA = gcr_sla)
        saveto_gas.save()

        return HttpResponseRedirect('/Request/Gas/')
    
class gasListView(ListView):
    model = Gas_card
    template_name = 'gas_card/gascard_list.html'

# class gasCreateView(SuccessMessageMixin, CreateView):
#     model = Gas_card
#     form_class = gascardform
#     template_name = 'gas_card/gascard_form.html'

#     def get_success_message(self, cleaned_data):
#         print(cleaned_data)
#         return "New Gas Card Details Has been Created!"

class gasUpdateView(SuccessMessageMixin, UpdateView):
    model = Gas_card
    form_class = gascardform
    template_name = 'gas_card/gascard_form.html'
    
    def get_success_message(self, cleaned_data):
    	print(cleaned_data)
    	return "Gas Card Details Update Successfully!"

class gasDetailView(DetailView):
    model = Gas_card
    template_name = 'gas_card/gascard_details.html'

class gasDeleteView(BSModalDeleteView):
    model = Gas_card
    template_name = 'gas_card/gascard_delete.html'
    success_message = 'Success: Gas Gard Request was deleted.'
    success_url = reverse_lazy('gascard_list')


                      #####################################  
                    #########################################
                   #####.     Service Vehicle Request    #####
                    #########################################
                     ######################################


class serviceListView(ListView):
    model = service_vehicle
    template_name = 'service_vehicle/service_list.html'

def serviceCreate(request):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    emplist = EmployeeMasterlist.objects.all()
    vlist = VehicleMasterList.objects.all()
    return render(request, 'service_vehicle/service_new.html',{'Title':'Car - Car Request', 'emplist':emplist,'vlist':vlist})

def servicesubmit(request):
    if request.method == 'POST':
        req_employee_id = request.POST.get('req_employee_id')
        request_date = request.POST.get('request_date')
        req_lname = request.POST.get('req_lname')
        req_fname = request.POST.get('req_fname')
        assignee_employee_id = request.POST.get('assignee_employee_id')
        Assignee_Group = request.POST.get('Assignee_Group')
        assignee_fname = request.POST.get('assignee_fname')
        assignee_lname = request.POST.get('assignee_lname')
        assignee_costcenter = request.POST.get('assignee_costcenter')
        assignee_section = request.POST.get('assignee_section')
        assignee_location = request.POST.get('assignee_location')
        assignee_atd = request.POST.get('assignee_atd')
        new_employee_id = request.POST.get('new_employee_id')
        new_employee_fname = request.POST.get('new_employee_fname')
        new_employee_lname = request.POST.get('new_employee_lname')
        new_employee_cost = request.POST.get('new_employee_cost')
        new_temporary_atd = request.POST.get('new_temporary_atd')
        prefered_vehicle = request.POST.get('prefered_vehicle')
        E_plate_no = request.POST.get('E_plate_no')
        E_con_sticker = request.POST.get('E_con_sticker')
        E_model_year = request.POST.get('E_model_year')
        E_brand = request.POST.get('E_brand')
        E_make = request.POST.get('E_make')
        E_type = request.POST.get('E_type')
        approved_by = request.POST.get('approved_by')
        approved_date = request.POST.get('approved_date')
        vehicle_provider = request.POST.get('vehicle_provider')
        vehicle_plate_no = request.POST.get('vehicle_plate_no')
        vehicle_CS_no = request.POST.get('vehicle_CS_no')
        vehicle_model = request.POST.get('vehicle_model')
        vehicle_brand = request.POST.get('vehicle_brand')
        vehicle_make = request.POST.get('vehicle_make')
        vehicle_fuel_type = request.POST.get('vehicle_fuel_type')
        svv_sla = request.POST.get('svv_sla')

        saveto_service = service_vehicle(request_date=request_date, req_employee_id=req_employee_id, req_lname=req_lname, req_fname =req_fname,
            asignee_employee_id=assignee_employee_id, assignee_group=Assignee_Group, assignee_fname=assignee_fname, assignee_lname=assignee_lname,
            assignee_costcenter=assignee_costcenter, assignee_section=assignee_section, assignee_location=assignee_location, assignee_atd=assignee_atd,
            new_employee_id=new_employee_id, new_employee_fname=new_employee_fname, new_employee_lname=new_employee_lname, new_employee_cost=new_employee_cost,
            new_temporary_atd=new_temporary_atd, prefered_vehicle=prefered_vehicle, E_plate_no=E_plate_no, E_con_sticker=E_con_sticker,
            E_model_year =E_model_year, E_brand=E_brand, E_make=E_make, E_type=E_type, approved_by=approved_by, approved_date=approved_date,
            vehicle_provider =vehicle_provider, vehicle_plate_no=vehicle_plate_no, vehicle_CS_no=vehicle_CS_no, vehicle_model =vehicle_model,
            vehicle_brand =vehicle_brand, vehicle_make=vehicle_make, vehicle_fuel_type=vehicle_fuel_type, SVV_SLA =svv_sla,)
        saveto_service.save()

        return HttpResponseRedirect('/Request/Service/')

class serviceCreateView(SuccessMessageMixin, CreateView):
    model = service_vehicle
    form_class = serviceform
    template_name = 'service_vehicle/service_form.html'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "New Service Vehicle Request Has been Created!"

class serviceUpdateView(SuccessMessageMixin, UpdateView):
    model = service_vehicle
    form_class = serviceform
    template_name = 'service_vehicle/service_form.html'
    
    def get_success_message(self, cleaned_data):
    	print(cleaned_data)
    	return "Service Vehicle Request Update Successfully!"

class serviceDetailView(DetailView):
    model = service_vehicle
    template_name = 'service_vehicle/service_details.html'

class serviceDeleteView(BSModalDeleteView):
    model = service_vehicle
    template_name = 'service_vehicle/service_delete.html'
    success_message = 'Success: Service Vehicle Request was deleted.'
    success_url = reverse_lazy('service_list')


                      #####################################  
                    #########################################
                   #####.     Vehicle Repair  Request    #####
                    #########################################
                     ######################################


class repairListView(ListView):
    model = Vehicle_Repair
    template_name='vehicle_repair/repair_list.html'
    
def repairCreate(request):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    emplist = EmployeeMasterlist.objects.all()
    vlist = VehicleMasterList.objects.all()
    return render(request, 'vehicle_repair/repair_new.html',{'Title':'Vehicle - Vehicle Repair','emplist':emplist,'vlist':vlist})

# class repairCreateView(SuccessMessageMixin, CreateView):
#     model = Vehicle_Repair
#     form_class = repairform
#     template_name = 'vehicle_repair/repair_form.html'

#     def get_success_message(self, cleaned_data):
#         print(cleaned_data)
#         return "New Vehicle Repair Request Has been Created!"

def repairsubmit(request):
    if request.method == 'POST':
        request_date = request.POST.get('request_date')
        emp_id = request.POST.get('emp_id')
        cost_center = request.POST.get('cost_center')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        c_no = request.POST.get('c_no')
        company = request.POST.get('company')
        department = request.POST.get('department')
        group = request.POST.get('group')
        plate_no = request.POST.get('plate_no')
        v_brand = request.POST.get('v_brand')
        engine = request.POST.get('engine')
        v_model = request.POST.get('v_model')
        v_make = request.POST.get('v_make')
        chassis = request.POST.get('chassis')
        v_band = request.POST.get('v_band')
        cs_no = request.POST.get('cs_no')
        eq_no = request.POST.get('eq_no')
        fleet_area = request.POST.get('fleet_area')
        particulars = request.POST.get('particulars')
        category = request.POST.get('category')
        maintenance_type1 = request.POST.get('maintenance_type1')
        maintenance_type2 = request.POST.get('maintenance_type2')
        scope_work1 = request.POST.get('scope_work1')
        scope_work2 = request.POST.get('scope_work2')
        recomendations = request.POST.get('recomendations')
        service_reminder = request.POST.get('service_reminder')
        repair_verified_by = request.POST.get('repair_verified_by')
        work_order1 = request.POST.get('work_order1')
        work_order2 = request.POST.get('work_order2')
        work_order3 = request.POST.get('work_order3')
        date_work_created = request.POST.get('date_work_created')
        repair_shop = request.POST.get('repair_shop')
        date_forward = request.POST.get('date_forward')
        estimate_no = request.POST.get('estimate_no')
        maintenance_amount = request.POST.get('maintenance_amount')
        less_discount = request.POST.get('less_discount')
        estimate_remark = request.POST.get('estimate_remark')
        estimate_attach = request.POST.get('estimate_attach')
        approved_by = request.POST.get('approved_by')
        kilo_reading = request.POST.get('kilo_reading')
        vrr_sla = request.POST.get('vrr_sla')

        saveto_repair = Vehicle_Repair(request_date=request_date, employee=emp_id, cost_center=cost_center, first_name=fname,
            last_name=lname, contact_no=c_no, company=company, department=department, group_section=group,
            plate_no=plate_no, v_brand=v_brand, engine=engine, v_make=v_make, v_model=v_model, chassis=chassis,
            band=v_band, cond_sticker=cs_no, equipment_no=eq_no, fleet_area=fleet_area, particulars=particulars,
            category=category, maintenance_type1=maintenance_type1, scope_work1=scope_work1, maintenance_type2=maintenance_type2,
            scope_work2=scope_work2, recommendations=recomendations, service_reminder=service_reminder, verified_by=repair_verified_by,
            work_order1=work_order1, work_order2=work_order2, work_order3=work_order3, datework_created=date_work_created,
            Shop_vendor=repair_shop, date_forwarded=date_forward, estimate_no=estimate_no, maintenance_amount=maintenance_amount,
            less_discount=less_discount, estimate_remarks=estimate_remark, estimate_attached=estimate_attach, approvedby=approved_by,
            meter_reading=kilo_reading,VRR_SLA=vrr_sla,
    )
        saveto_repair.save()

        return HttpResponseRedirect('/Request/Repair/')

class repairDetailView(DetailView):
    model = Vehicle_Repair
    template_name = 'vehicle_repair/repair_details.html'

class repairUpdateView(SuccessMessageMixin, UpdateView):
    model = Vehicle_Repair
    form_class = repairform
    template_name = 'vehicle_repair/repair_form.html'
    
    def get_success_message(self, cleaned_data):
    	print(cleaned_data)
    	return "Vehicle Repair Request Updated Successfully!"

class repairDeleteView(BSModalDeleteView):
    model = Vehicle_Repair
    template_name = 'vehicle_repair/repair_delete.html'
    success_message = 'Success: Vehicle Repair Request was deleted.'
    success_url = reverse_lazy('repair_list')



