from django.urls import path
from . import views
from .views import (
	employeeListView,
	vehicleMasterListView,
	)

urlpatterns = [
	path('EmployeeMasterlist/New', views.employeeMasterlist, name='employeeMasterlist-new'),
	path('Employee/', employeeListView.as_view(), name='employee-list'),
	# path('Employee/', views.employeeList, name='employee-list'),
	path('VehicleMasterlist/', vehicleMasterListView.as_view(), name='vehicle-list'),
	path('VehicleMasterlist/New', views.vehicleMasterlist, name='vehicleMasterlist-new'),
	#path('VehicleMasterlist/', views.VehicleList, name='vehicle-list'),
]