from django.urls import path
from . import views
# from .views import (
# 	CarRentalDetailView
# )

urlpatterns = [
	path('CarRental/', views.Vehicle_list, name='Vehicle_list'),
	path('Vehicle/new', views.VehicleCreate, name='Vehicle-new'),
	path('Car/', views.Car, name='carrental_list'),
	path('Car/new', views.Carrentalpayment, name='Car-rental'),
	path('Carrental/submit', views.Carrental_submit, name='Car_submit'),
	#path('Carrental/<int:pk>', CarRentalDetailView.as_view(), name='Carrental_summary'),

]