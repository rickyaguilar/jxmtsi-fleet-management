from django.urls import path
from . import views
from .views import (
  	CarRentalDetailView,
	carrentalDeleteView,
	CarListView,
  	VehicleListView,
  	VehicleDetailView,
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
	# path('Vehicle/New', VehicleCreateView.as_view(),name='Vehicle-new'),
	path('Vehicle/New', views.vehiclecreate, name='Vehicle-new'),
	path('Vehicle/submit', views.vehicle_submit, name='Vehicle_submit'),
	path('Vehicle/Detail/<int:pk>', VehicleDetailView.as_view(), name='Vehicle-summary'),
	path('Vehicle/Update/<int:pk>', VehicleUpdateView.as_view(), name='Vehicle-update'),
	path('Vehicle/Delete/<int:pk>', VehicleDeleteView.as_view(), name='Vehicle_delete'),
	path('Vehicle/History/', views.VehicleHistoryView, name='Vehicle_history'),
	path('Vehicle/export', views.vehicle_excel, name='vehicle_export'),
	path('Car/', CarListView.as_view(), name='carrental_list'),
	path('Car/New', views.Carrentalpayment, name='Car-rental'),
	path('Car/Submit', views.Carrental_submit, name='Car_submit'),
	path('Car/Detail/<int:pk>', CarRentalDetailView.as_view(), name='Carrental_summary'),
	path('Car/Update/<int:pk>', views.Carrental_update, name='Car_update'),
	path('Car/Delete/<int:pk>', carrentalDeleteView.as_view(), name='carrental_delete'),
	path('Car/History/', views.carrentalHistoryView, name='carrental_history'),
	path('Car/export', views.car_excel, name = 'car_export'),
	path('Fuel/', FuelListView.as_view(), name = 'Fuel_supplierList'),
	path('Fuel/New', FuelCreateView.as_view(), name='Fuel_supplierNew'),
	path('Fuel/Update/<int:pk>', FuelUpdateView.as_view(), name='Fuel_update'),
	path('Fuel/Detail/<int:pk>', FuelDetailView.as_view(), name='Fuel-summary'),
	path('Fuel/Delete/<int:pk>', FuelDeleteView.as_view(), name='Fuel_delete'),
	path('Fuel/History/', views.FuelHistoryView, name='Fuel_history'),
	path('Fuel/export', views.fuel_excel, name='fuel_export')

]