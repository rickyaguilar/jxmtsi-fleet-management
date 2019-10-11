from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import (
     ListView,
 )
from .models import (
	EmployeeMasterlist,
	VehicleMasterList,
	)

def employeeMasterlist(request):
#    @method_decorator(user_passes_test(in_group))
    def dispatch(self, *args, **kwargs):
       return super().dispatch(*args, **kwargs)
    return render(request, 'employeeMasterlist/employeeMasterlist_form.html')

class employeeListView(ListView):
	model = EmployeeMasterlist
	template_name = 'employeeMasterlist/employeeMasterlist.html'

# def employeeList(request):
# 	model = EmployeeMasterlist
# 	employee_list = EmployeeMasterlist.objects.all()
# 	return render(request, 'employeeMasterlist/employeeMasterlist.html', {'title': 'Employee Master List', 'employee_list': employee_list})

def vehicleMasterlist(request):
#    @method_decorator(user_passes_test(in_group))
    def dispatch(self, *args, **kwargs):
       return super().dispatch(*args, **kwargs)
    return render(request, 'vehicleMasterlist/vehicleMasterlist_form.html')

class vehicleMasterListView(ListView):
	model = VehicleMasterList
	template_name = 'vehicleMasterlist/vehicleMasterlist.html'

# def VehicleList(request):
# 	model = VehicleMasterList
# 	vehicle_list = VehicleMasterList.objects.all()
# 	return render(request, 'masterlist/vehicleMasterlist/vehicleMasterlist.html', {'title': 'Vehicle Master List', 'vehicle_list': vehicle_list})
