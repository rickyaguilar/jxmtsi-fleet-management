from django.shortcuts import render,HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import (
   	Ownership,
)
from . forms import (
    ownershipForm
)
from django.views.generic import (
                				CreateView,
                				ListView,
                				UpdateView,
                				DetailView,
                				)
from bootstrap_modal_forms.generic import (
                                           BSModalDeleteView
                                           )

class ownershipListView(ListView):
	model = Ownership
	template_name = 'transfer_list.html'


class ownershipCreateView(SuccessMessageMixin, CreateView):
	def dispatch(self, *args, **kwargs):
	    return super().dispatch(*args, **kwargs)
	template_name = 'transfer_form.html'
	form_class = ownershipForm

	def get_success_message(self, cleaned_data):
		print(cleaned_data)
		return "New Transfer of Ownership Has been Created!"

class ownershipUpdate(SuccessMessageMixin, UpdateView):
	model = Ownership
	form_class = ownershipForm
	template_name = 'transfer_form.html'

	def get_success_message(self, cleaned_data):
		print(cleaned_data)
		return "Transfer of Ownership Updated Successfully!"
		
class ownershipDetails(DetailView):
	model = Ownership
	template_name = 'transfer_details.html'
	
class ownershipDeleteView(BSModalDeleteView):
    model = Ownership
    template_name = 'transfer_delete.html'
    success_message = 'Success: Item was deleted.'
    success_url = reverse_lazy('ownership_list')