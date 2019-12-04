from django.urls import path
from . import views
from .views import (
  	CarRentalDetailView,
	carrentalDeleteView,
	CarListView,
  	VehicleListView,
  	VehicleDetailView,
  	VehicleCreateView,
  	VehicleUpdateView,
	VehicleDeleteView,
  	FuelCreateView,
  	FuelUpdateView,
  	FuelListView,
	FuelDetailView,
	FuelDeleteView,
	
 )

urlpatterns = [
	path('Vehicle/', VehicleListView.as_view(), name = 'Vehicle_list'),
	path('Vehicle/New', VehicleCreateView.as_view(),name='Vehicle-new'),
	path('Vehicle/Detail/<int:pk>', VehicleDetailView.as_view(), name='Vehicle-summary'),
	path('Vehicle/Update/<int:pk>', VehicleUpdateView.as_view(), name='Vehicle-update'),
	path('Vehicle/Delete/<int:pk>', VehicleDeleteView.as_view(), name='Vehicle_delete'),
	path('Car/', CarListView.as_view(), name='carrental_list'),
	path('Car/New', views.Carrentalpayment, name='Car-rental'),
	path('Car/Submit', views.Carrental_submit, name='Car_submit'),
	path('Car/Detail/<int:pk>', CarRentalDetailView.as_view(), name='Carrental_summary'),
	path('Car/Update/<int:pk>', views.Carrental_update, name='Car_update'),
	path('Car/Delete/<int:pk>', carrentalDeleteView.as_view(), name='carrental_delete'),
	path('Fuel/', FuelListView.as_view(), name = 'Fuel_supplierList'),
	path('Fuel/New', FuelCreateView.as_view(), name='Fuel_supplierNew'),
	path('Fuel/Update/<int:pk>', FuelUpdateView.as_view(), name='Fuel_update'),
	path('Fuel/Detail/<int:pk>', FuelDetailView.as_view(), name='Fuel-summary'),
	path('Fuel/Delete/<int:pk>', FuelDeleteView.as_view(), name='Fuel_delete')

]