from django.shortcuts import render,HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import (
   	Fata_monitoring,
)
from . forms import (
    FATAmonitoringForm
)
from django.views.generic import (
                				DetailView,
                				)

		
class monitoringDetails(DetailView):
	model = Fata_monitoring
	template_name = 'fata_monitoring_details.html'
	
