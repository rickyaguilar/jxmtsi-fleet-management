from django.views import generic
from django.shortcuts import render,HttpResponseRedirect, get_list_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import (
		CarRentalRequest,
        Gas_card,
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