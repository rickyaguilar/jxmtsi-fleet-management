from django.urls import path
from . import views
from .views import (
  	CarRentalDetailView,
  	VehicleListView,
  	FuelListView,
  	CarListView,
  	VehicleDetailView,
  	FuelDetailView,
  	VehicleCreateView,
  	VehicleUpdateView,
  	FuelCreateView,
  	FuelUpdateView,
 )

urlpatterns = [
	path('Vehicle/', VehicleListView.as_view(), name = 'Vehicle_list'),
	path('Vehicle/New', VehicleCreateView.as_view(),name='Vehicle-new'),
	path('Vehicle/Detail/<int:pk>', VehicleDetailView.as_view(), name='Vehicle-summary'),
	path('Vehicle/Update/<int:pk>', VehicleUpdateView.as_view(), name='Vehicle-update'),
	path('Car/', CarListView.as_view(), name='carrental_list'),
	path('Car/New', views.Carrentalpayment, name='Car-rental'),
	# path('Car/New', CarrentalCreateView.as_view(), name='Car-rental'),
	path('Carrental/Submit', views.Carrental_submit, name='Car_submit'),
	path('CarSummary/Detail/<int:pk>', CarRentalDetailView.as_view(), name='Carrental_summary'),
	path('CarUpdate/Update/<int:pk>', views.Carrental_update, name='Car_update'),
	path('Fuel/', FuelListView.as_view(), name = 'Fuel_supplierList'),
	path('Fuel/New', FuelCreateView.as_view(), name='Fuel_supplierNew'),
	path('Fuel/Update/<int:pk>', FuelUpdateView.as_view(), name='Fuel_update'),
	path('Fuel/Detail/<int:pk>', FuelDetailView.as_view(), name='Fuel-summary')

]