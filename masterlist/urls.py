from django.urls import path
from . import views
from .views import (
	employeeListView,
	employeeCreateView,
	employeeDetailView,
	employeeUpdateView,
	vehicleMasterListView,
	VmasterlistCreateView,
	vehicleMasterDetails,
	vehicleMasterUpdate,

	)

urlpatterns = [
	path('EmployeeMasterlist/', employeeListView.as_view(), name='employee-list'),
	path('EmployeeMasterlist/New', employeeCreateView.as_view(), name='employeeMasterlist-new'),
	path('EmployeeMasterlist/Detail/<int:pk>', employeeDetailView.as_view(), name='employee-details'),
	path('EmployeeMasterlist/Update/<int:pk>', employeeUpdateView.as_view(), name='employeeMasterlist-update'),
	path('VehicleMasterlist/', vehicleMasterListView.as_view(), name='vehicle-list'),
	path('VehicleMasterlist/New', VmasterlistCreateView.as_view(), name='vehicleMasterlist-new'),
	path('VehicleMasterlist/Details/<int:pk>', vehicleMasterDetails.as_view(), name='vehicle-details'),
	path('VehicleMasterlist/Update/<int:pk>', vehicleMasterUpdate.as_view(),name='vehicle-update'),
]