from django.shortcuts import render,HttpResponseRedirect, render
from .models import (
    CarRental,
)
# from django.views.generic import (
#     DetailView
# )
#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import user_passes_test



#def in_group(user):
#    if user.groups.filter(name="Driver").exists():
#        return True
#    else:
#        raise PermissionDenied()

def Car(request):
	Car_rental_list = CarRental.objects.all()
	return render(request, 'payment/carrental_list.html', {'title':'Car Rental Payment','Car_rental_list': Car_rental_list})

def Carrentalpayment(request):
#    @method_decorator(user_passes_test(in_group))
#    def dispatch(self, *args, **kwargs):
#        return super().dispatch(*args, **kwargs)
    return render(request, 'payment/car_rental.html')

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


		saveto_CRP = CarRental(Bill_date=Bill_date,Employee_id=employee_id, L_name=lastname, F_name=firstname,
			Assignee_company=Ass_company, Cost_center=Cost_center, O_Fname=Other_assigneeFM, O_Lname=Other_assigneeLM,
			O_cost_center=Other_cost, Plate_no=Plate_no, V_provider=V_provider, V_brand=V_brand, V_make=V_make,
			D_vehicle=Delivered_V, S_rental=S_rental, E_rental=E_rental, R_duration=Rduration, R_Cost=R_cost,
			G_cost=Gas_cost, T_fee=Toll_fee, P_fee=Park_fee, Del_fee=Del_fee, Dri_fee=Driverfee, M_cost=Meal_cost,
			O_expenses=Other_exp, T_expenses=Total, Date_initiated=Date_initiated)
		saveto_CRP.save()

		return HttpResponseRedirect('/Payment/Car/')

# class CarRentalDetailView(DetailView):
# 	#@method_decorator(user_passes_test(in_group))
# 	def dispatch(self, *args, **kwargs):
# 		return super().dispatch(*args, **kwargs)
# 	model = CarRental
# 	template_name = 'Car_rental/carrental_summary.html'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['rental'] = CarRental.objects.filter(Activity_id=self.object.pk)
# 		context['Crental'] = CarRental.objects.all()
# 		return context

def VehicleCreate(request):
#    @method_decorator(user_passes_test(in_group))
#    def dispatch(self, *args, **kwargs):
#        return super().dispatch(*args, **kwargs)
    return render(request, 'payment/vehiclepayment_new.html')

#@user_passes_test(in_group)
def Vehicle_list(request):
	#Car_rental_list = CarRental.objects.all()
	return render(request, 'payment/vehicle_list.html', {'title':'','Vehicle list': Vehicle_list})





