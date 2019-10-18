from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import (
    CarRental,
    VehiclePayment,
    Fuel_supplier,
)
from django.views.generic import (
     DetailView,
     ListView,
     CreateView,
     UpdateView,
 )
from . forms import (
    VehiclePaymentform,
    FuelsupplierForm
)

# class CarrentalCreateView(CreateView):
#     model = CarRental
#     form_class = CarRentalForm
#     template_name = 'payment/car/carsample.html'

class CarListView(ListView):
	model = CarRental
	template_name = 'payment/car/carrental_list.html'
	
class CarRentalDetailView(DetailView):
	model = CarRental
	template_name = 'payment/car/carrental_summary.html'

def Carrentalpayment(request):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    return render(request, 'payment/car/car_rental.html')

def Carrental_submit(request):
	if request.method == 'POST':
		#<---Assign Details--->
		Bill_date = request.POST.get('Bdate')
		employee_id = request.POST.get('Eid')
		firstname = request.POST.get('Efm')
		lastname = request.POST.get('Elm')
		Ass_company = request.POST.get('Acom')
		Cost_center = request.POST.get('Acost')
		Date_initiated = request.POST.get('date')
		#<-- other assign-->
		Other_assigneeFM = request.POST.get('Ofname')
		Other_assigneeLM = request.POST.get('Olname')
		Other_cost = request.POST.get('Ocost')
		#<--Vehicle Details-->
		Plate_no = request.POST.get('Pnumber')
		V_provider = request.POST.get('Vprovider')
		V_brand = request.POST.get('Vbrand')
		V_make = request.POST.get('Vmake')
		#<--Rental Details-->
		Delivered_V = request.POST.get('Ddelivered')
		S_rental = request.POST.get('Srental')
		E_rental = request.POST.get('Erental')
		Rduration = request.POST.get('Rduration')
		#<--Expense Details-->
		R_cost = request.POST.get('Rcost')
		Gas_cost = request.POST.get('Gcost')
		Toll_fee = request.POST.get('Tfee')
		Park_fee = request.POST.get('Pfee')
		Del_fee = request.POST.get('Dfee')
		Driverfee = request.POST.get('Driverfee')
		Meal_cost = request.POST.get('M_cost')
		Other_exp = request.POST.get('Other_exp')
		Total = request.POST.get('Total')
		C_SLA = request.POST.get('SLA')


		saveto_CRP = CarRental(Bill_date=Bill_date,Employee_id=employee_id, L_name=lastname, F_name=firstname,
			Assignee_company=Ass_company, Cost_center=Cost_center, O_Fname=Other_assigneeFM, O_Lname=Other_assigneeLM,
			O_cost_center=Other_cost, Plate_no=Plate_no, V_provider=V_provider, V_brand=V_brand, V_make=V_make,
			D_vehicle=Delivered_V, S_rental=S_rental, E_rental=E_rental, R_duration=Rduration, R_Cost=R_cost,
			G_cost=Gas_cost, T_fee=Toll_fee, P_fee=Park_fee, Del_fee=Del_fee, Dri_fee=Driverfee, M_cost=Meal_cost,
			O_expenses=Other_exp, T_expenses=Total, Date_initiated=Date_initiated, C_SLA=C_SLA)
		saveto_CRP.save()

		return HttpResponseRedirect('/Payment/Car/')

def Carrental_update(request, pk):
	if request.method == 'POST':
		#<---Assign Details--->
		Bill_date = request.POST.get('Bdate')
		employee_id = request.POST.get('Eid')
		firstname = request.POST.get('Efm')
		lastname = request.POST.get('Elm')
		Ass_company = request.POST.get('Acom')
		Cost_center = request.POST.get('Acost')
		#<-- other assign-->
		Other_assigneeFM = request.POST.get('Ofname')
		Other_assigneeLM = request.POST.get('Olname')
		Other_cost = request.POST.get('Ocost')
		#<--Vehicle Details-->
		Plate_no = request.POST.get('Pnumber')
		V_provider = request.POST.get('Vprovider')
		V_brand = request.POST.get('Vbrand')
		V_make = request.POST.get('Vmake')
		#<--Rental Details-->
		Delivered_V = request.POST.get('Ddelivered')
		S_rental = request.POST.get('Srental')
		E_rental = request.POST.get('Erental')
		Rduration = request.POST.get('Rduration')
		#<--Expense Details-->
		R_cost = request.POST.get('Rcost')
		Gas_cost = request.POST.get('Gcost')
		Toll_fee = request.POST.get('Tfee')
		Park_fee = request.POST.get('Pfee')
		Del_fee = request.POST.get('Dfee')
		Driverfee = request.POST.get('Driverfee')
		Meal_cost = request.POST.get('M_cost')
		Other_exp = request.POST.get('Other_exp')
		Total = request.POST.get('Total')


		CarRental.objects.filter(id=pk).update(Bill_date=Bill_date,Employee_id=employee_id, L_name=lastname, F_name=firstname,
			Assignee_company=Ass_company, Cost_center=Cost_center, O_Fname=Other_assigneeFM, O_Lname=Other_assigneeLM,
			O_cost_center=Other_cost, Plate_no=Plate_no, V_provider=V_provider, V_brand=V_brand, V_make=V_make,
			D_vehicle=Delivered_V, S_rental=S_rental, E_rental=E_rental, R_duration=Rduration, R_Cost=R_cost,
			G_cost=Gas_cost, T_fee=Toll_fee, P_fee=Park_fee, Del_fee=Del_fee, Dri_fee=Driverfee, M_cost=Meal_cost,
			O_expenses=Other_exp, T_expenses=Total)

		return HttpResponseRedirect('/Payment/Car/')

class VehicleCreateView(SuccessMessageMixin, CreateView):
    model = VehiclePayment
    form_class = VehiclePaymentform
    template_name = 'payment/vehicle/vehiclepayment_new.html'

    def get_success_message(self, cleaned_data):
    	print(cleaned_data)
    	return "New Vehicle Payment's Has been Created!"

class VehicleListView(ListView):
	model = VehiclePayment
	template_name = 'payment/vehicle/vehicle_list.html'

class VehicleDetailView(DetailView):
	model = VehiclePayment
	template_name = 'payment/vehicle/vehiclepayment_summary.html'

class VehicleUpdateView(SuccessMessageMixin, UpdateView):
    model = VehiclePayment
    form_class = VehiclePaymentform
    template_name = 'payment/vehicle/vehiclepayment_new.html'

    def get_success_message(self, cleaned_data):
    	print(cleaned_data)
    	return "New Vehicle Payment's Update Successfully!"
			

class FuelDetailView(DetailView):
	model = Fuel_supplier
	template_name = 'payment/fuel/fuel_supplierSummary.html'

class FuelListView(ListView):
	model = Fuel_supplier
	template_name = 'payment/fuel/fuel_supplierList.html'

class FuelCreateView(SuccessMessageMixin, CreateView):
    model = Fuel_supplier
    form_class = FuelsupplierForm
    template_name = 'payment/fuel/fuel_supplier.html'

    def get_success_message(self, cleaned_data):
    	print(cleaned_data)
    	return "Fuel Supplier Has been Created!"

class FuelUpdateView(SuccessMessageMixin, UpdateView):
    model = Fuel_supplier
    form_class = FuelsupplierForm
    template_name = 'payment/fuel/fuel_supplier.html'

    def get_success_message(self, cleaned_data):
    	print(cleaned_data)
    	return "Fuel Supplier Update Successfully!"




