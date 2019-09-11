from django.urls import path
from . import views
from .views import (
	DriverCreateView
)

urlpatterns = [
	path('Driver/', views.Drivers, name='driver_list'),
	path('Driver/new', DriverCreateView.as_view(), name='Drivers-new'),


]