from django.urls import path
from . import views
from .views import (
	monitoringCreateView,
	monitoringListView,
	)

urlpatterns = [
	path('Monitoring/', monitoringListView.as_view(), name= 'Monitoring_list'),
	path('Monitoring/new', monitoringCreateView.as_view(), name='Monitoring_new'),

]