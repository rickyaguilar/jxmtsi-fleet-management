
from django.urls import path
from . import views
from .views import (
	employeeListView,
	employeeCreateView,
	employeeDetailView,
	employeeUpdateView,
	employeeMasterlistDeleteView,
	# vehicleMasterListView,
	# VmasterlistCreateView,
	vehicleMasterDetails,
	vehicleMasterUpdate,
	vehicleMasterlistDeleteView,

	)


urlpatterns = [
	path('EmployeeMasterlist/', employeeListView.as_view(), name='employee-list'),
	path('EmployeeMasterlist/New', employeeCreateView.as_view(), name='employeeMasterlist-new'),
	path('EmployeeMasterlist/Detail/<int:pk>', employeeDetailView.as_view(), name='employee-details'),
	path('EmployeeMasterlist/Update/<int:pk>', employeeUpdateView.as_view(), name='employeeMasterlist-update'),
	path('EmployeeMasterlist/Delete/<int:pk>', employeeMasterlistDeleteView.as_view(), name='employeeMasterlist_delete'),
	path('Masterlist/export', views.employee_excel, name='masterlist_dl'),
	# path('VehicleMasterlist/', vehicleMasterListView.as_view(), name='vehicle-list'),
	path('VehicleMasterlist/', views.Vmastertables, name='vehicle-list'),
	path('VehicleMasterlist/New', views.vehicle, name='vehicle_new'),
	path('VehicleMasterlist/submit', views.VmasterlistCreate, name='vehicleMasterlist_submit'),
	path('VehicleMasterlist/Details/<int:pk>', vehicleMasterDetails.as_view(), name='vehicle-details'),
	path('VehicleMasterlist/Update/<int:pk>', vehicleMasterUpdate.as_view(),name='vehicle-update'),
	path('VehicleMasterlist/Delete/<int:pk>', vehicleMasterlistDeleteView.as_view(), name='vehicleMasterlist_delete'),
	path('Vehicle/<int:pk>', views.releaseUpdate.as_view(), name='vupdate'),
	path('Vehiclelist/export', views.vehicle_excel, name='vehiclelist_export'),
	path('Vehicle/filter', views.registration, name='vehiclefilter'),
]







