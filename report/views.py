from django.shortcuts import render,HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import (
   	vehicle_report,
)
# from masterlist.models import EmployeeMasterlist,VehicleMasterList
# from . forms import (
#     voucherform,
# )
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

class reportListView(ListView):
	model = vehicle_report
	template_name = 'report_list.html'