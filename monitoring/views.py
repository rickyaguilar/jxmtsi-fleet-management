from django.shortcuts import render,HttpResponseRedirect
from .models import (
   	Fata_monitoring,
)
from . forms import (
    FATAmonitoringForm
)
from django.views.generic import (
                				CreateView,
                				ListView,
                				)

class monitoringListView(ListView):
	model = Fata_monitoring
	template_name = 'fata_monitoringlist.html'


class monitoringCreateView(CreateView):
	def dispatch(self, *args, **kwargs):
	    return super().dispatch(*args, **kwargs)
	template_name = 'fata_monitoring.html'
	form_class = FATAmonitoringForm