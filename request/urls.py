from django.urls import path
from . import views
from .views import (
  	requestCreateView,
  	requestListView,
	requestDetailView,
	requestUpdateView,
	requestDeleteView,
	gasListView,
	gasCreateView,
	gasUpdateView,
	gasDetailView,
	gasDeleteView,
	serviceListView,
	serviceCreateView,
	serviceUpdateView,
	serviceDetailView,
 )

urlpatterns = [
	path('Request/', requestListView.as_view(), name='carrequest_list'),
	path('Request/New', requestCreateView.as_view(), name='car_request'),
	path('Request/Details/<int:pk>/', requestDetailView.as_view(), name='carrequest_details'),
	path('Request/Update/<int:pk>/', requestUpdateView.as_view(), name='carrequest_update'),
	path('Request/Delete/<int:pk>/', requestDeleteView.as_view(), name='carrequest_delete'),
	path('Gas/', gasListView.as_view(),name='gascard_list'),
	path('Gas/New', gasCreateView.as_view(), name='gascard_new'),
	path('Gas/Update/<int:pk>', gasUpdateView.as_view(), name='gascard_update'),
	path('Gas/Details/<int:pk>', gasDetailView.as_view(), name='gascard_details'),
	path('Gas/Delete/<int:pk>', gasDeleteView.as_view(), name='gascard_delete'),
	path('Service/', serviceListView.as_view(), name='service_list'),
	path('Service/New', serviceCreateView.as_view(), name='service_new'),
	path('Service/Details/<int:pk>', serviceDetailView.as_view(), name='service_details'),
	path('Service/Update/<int:pk>', serviceUpdateView.as_view(), name='service_update')

	]