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


class requestCreateView(SuccessMessageMixin, CreateView):
    model = CarRentalRequest
    form_class = carrequestform
    template_name = 'car_rental/carrequest_form.html'

    def get_success_message(self, cleaned_data):
    	print(cleaned_data)
    	return "New Car Rental Request Has been Created!"

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

class gasListView(ListView):
    model = Gas_card
    template_name = 'gas_card/gascard_list.html'

class gasCreateView(SuccessMessageMixin, CreateView):
    model = Gas_card
    form_class = gascardform
    template_name = 'gas_card/gascard_form.html'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "New Gas Card Details Has been Created!"

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


class serviceListView(ListView):
    model = service_vehicle
    template_name = 'service_vehicle/service_list.html'

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

class repairListView(ListView):
    model = Vehicle_Repair
    template_name='vehicle_repair/repair_list.html'

class repairCreateView(SuccessMessageMixin, CreateView):
    model = Vehicle_Repair
    form_class = repairform
    template_name = 'vehicle_repair/repair_form.html'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "New Vehicle Repair Request Has been Created!"

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


