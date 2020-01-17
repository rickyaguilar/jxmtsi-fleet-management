from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy
import datetime
from ajax_select import register, LookupChannel
from .models import (
   	vehicle_report,
	VehicleMasterList,
)
from . forms import (
    reportform,
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


class reportListView(ListView):
	model = vehicle_report
	template_name = 'report_list.html'

# def report_submit(request):
# 	if request.method == 'POST':
# 		mvar_date = request.POST.get('mvar_date')
# 		acc_type = request.POST.get('acc_type')
# 		supp_docs = request.POST.get('supp_docs')
# 		plate_number = request.POST.get('plate_number')
# 		v_model = request.POST.get('v_model')
# 		v_make = request.POST.get('v_make')
# 		c_sticker = request.POST.get('c_sticker')
# 		a_emp_id = request.POST.get('a_emp_id')
# 		a_emp_fname = request.POST.get('a_emp_fname')
# 		a_emp_lname = request.POST.get('a_emp_lname')
# 		a_emp_number = request.POST.get('a_emp_number')
# 		a_emp_company = request.POST.get('a_emp_company')
# 		a_emp_group = request.POST.get('a_emp_group')
# 		a_emp_div = request.POST.get('a_emp_div')
# 		a_emp_dept = request.POST.get('a_emp_dept')
# 		ai_emp_id = request.POST.get('ai_emp_id')
# 		ai_emp_fname = request.POST.get('ai_emp_fname')
# 		ai_emp_lname = request.POST.get('ai_emp_lname')
# 		inform_inspection = request.POST.get('inform_inspection')
# 		date_inspection = request.POST.get('date_inspection')
# 		inspection_remarks = request.POST.get('inspection_remarks')
# 		date_filed = request.POST.get('date_filed')
# 		date_received = request.POST.get('date_received')
# 		date_forward = request.POST.get('date_forward')
# 		SLA = request.POTS.get('SLA')
# 		date_initiated = datetime.date.today()

# 		saveto_report = vehicle_report(received_date=mvar_date, v_accident_type=acc_type, support_docs=supp_docs, plate_number=plate_number, v_model=v_model, v_make=v_make, 
# 			cond_sticker=c_sticker, a_employee_id=a_emp_id, a_employee_fname=a_emp_fname, a_employee_lname=a_emp_lname, a_employee_no=a_emp_number, a_employee_company=a_emp_company, a_employee_group=a_emp_group, 
# 			a_employee_division=a_emp_div, a_employee_dept=a_emp_dept, sup_employee_id=ai_emp_id, sup_employee_fname=ai_emp_fname, sup_employee_lname=ai_emp_lname, inform_assignee=inform_inspection, 
# 			date_of_inspection=date_inspection, inspection_remarks=inspection_remarks, date_filed_alarm=date_filed, date_cert_received=date_received, date_forwarded=date_forward, MVAR_SLA=SLA, date_initiated=date_initiated)
# 		saveto_report.save()

# 		return HttpResponseRedirect('/Report/Report/')

class reportCreateView(SuccessMessageMixin, CreateView):
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)
	template_name = 'report_form.html'
	form_class = reportform

	def get_success_message(self, cleaned_data):
		print(cleaned_data)
		return "New Vehicle Report Has been Created!"                                                                                           

class reportUpdate(SuccessMessageMixin, UpdateView):
	model = vehicle_report
	form_class = reportform
	template_name = 'report_form.html'

	def get_success_message(self, cleaned_data):
		print(cleaned_data)
		return "Vehicle Report Updated Successfully!"

class reportDetails(DetailView):
	model = vehicle_report
	template_name = 'report_details.html'
	
class reportDeleteView(BSModalDeleteView):
    model = vehicle_report
    template_name = 'report_delete.html'
    success_message = 'Success: Report Vehicle was deleted.'
    success_url = reverse_lazy('report_list')


@register('VehicleMasterList')
class vehicleLookup(LookupChannel):
    
    model = VehicleMasterList

    def get_query(self, q, request):
        return self.model.objects.filter(Plate_no__icontains=q).order_by('Plate_no')[:50]

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.Plate_no


        