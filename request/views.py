from django.views import generic
from django.shortcuts import render,HttpResponseRedirect, get_list_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import (
		CarRentalRequest,
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