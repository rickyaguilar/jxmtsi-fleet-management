from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse_lazy
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
	Vmasterlist
	)

class VmasterlistCreateView(CreateView):
	model = VehicleMasterList
	form_class = Vmasterlist
	template_name = 'vehicleMasterlist/vehicleMasterlist_form.html'

class vehicleMasterListView(ListView):
	model = VehicleMasterList
	template_name = 'vehicleMasterlist/vehicleMasterlist.html'

class vehicleMasterDetails(DetailView):
	model = VehicleMasterList
	template_name = 'vehicleMasterlist/vehicleMasterlist_details.html'

class vehicleMasterUpdate(UpdateView):
	model = VehicleMasterList
	form_class = Vmasterlist
	template_name = 'vehicleMasterlist/vehicleMasterlist_form.html'

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










