from django.shortcuts import render,HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import (
   	expense_voucher,
)
from masterlist.models import EmployeeMasterlist,VehicleMasterList
from . forms import (
    voucherform,
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

# def voucher(request):
# 	employee_list = EmployeeMasterlist.objects.all()
# 	vehicle_list = VehicleMasterList.objects.all()
# 	return render(request, 'voucher_form.html', {'title': 'Voucher - Create New Expense Voucher', 'employee_list': employee_list, 
# 	'vehicle_list': vehicle_list})

class voucherListView(ListView):
	model = expense_voucher
	template_name = 'voucher_list.html'


class voucherCreateView(SuccessMessageMixin, CreateView):
	def dispatch(self, *args, **kwargs):
	    return super().dispatch(*args, **kwargs)
	template_name = 'voucher_form.html'
	form_class = voucherform

	def get_success_message(self, cleaned_data):
		print(cleaned_data)
		return "New Expense Voucher Has been Created!"

class voucherUpdate(SuccessMessageMixin, UpdateView):
	model = expense_voucher
	form_class = voucherform
	template_name = 'voucher_form.html'

	def get_success_message(self, cleaned_data):
		print(cleaned_data)
		return "Expense Voucher Updated Successfully!"
		
class voucherDetails(DetailView):
	model = expense_voucher
	template_name = 'voucher_details.html'
	
class voucherDeleteView(BSModalDeleteView):
    model = expense_voucher
    template_name = 'voucher_delete.html'
    success_message = 'Success: Expense Voucher was deleted.'
    success_url = reverse_lazy('voucher_list')