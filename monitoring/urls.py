from django.urls import path
from . import views
from .views import (
	monitoringCreateView,
	monitoringListView,
	monitoringUpdate,
	monitoringDetails,
	monitoringDeleteView,

	)

urlpatterns = [
	path('Monitoring/', monitoringListView.as_view(), name= 'Monitoring_list'),
	path('Monitoring/new', monitoringCreateView.as_view(), name='Monitoring_new'),
	path('Monitoring/Update/<int:pk>', monitoringUpdate.as_view(), name='Monitoring_update'),
	path('Monitoring/Details/<int:pk>', monitoringDetails.as_view(), name='Monitoring_details'),
	path('Monitoring/Delete/<int:pk>', monitoringDeleteView.as_view(), name='Monitoring_delete'),
]