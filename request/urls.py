from django.urls import path
from . import views

urlpatterns = [
	path('Request/', views.requestListView.as_view(), name='carrequest_list'),
	path('Request/New', views.requestCreateView.as_view(), name='car_request'),
	path('Request/Details/<int:pk>/', views.requestDetailView.as_view(), name='carrequest_details'),
	path('Request/Update/<int:pk>/', views.requestUpdateView.as_view(), name='carrequest_update'),
	path('Request/Delete/<int:pk>/', views.requestDeleteView.as_view(), name='carrequest_delete'),
	path('Gas/', views.gasListView.as_view(),name='gascard_list'),
	path('Gas/New', views.gasCreateView.as_view(), name='gascard_new'),
	path('Gas/Update/<int:pk>', views.gasUpdateView.as_view(), name='gascard_update'),
	path('Gas/Details/<int:pk>', views.gasDetailView.as_view(), name='gascard_details'),
	path('Gas/Delete/<int:pk>', views.gasDeleteView.as_view(), name='gascard_delete'),
	path('Service/', views.serviceListView.as_view(), name='service_list'),
	path('Service/New', views.serviceCreateView.as_view(), name='service_new'),
	path('Service/Details/<int:pk>', views.serviceDetailView.as_view(), name='service_details'),
	path('Service/Update/<int:pk>', views.serviceUpdateView.as_view(), name='service_update'),
	path('Service/Delete/<int:pk>', views.serviceDeleteView.as_view(), name='service_delete'),
	path('Repair/', views.repairListView.as_view(), name='repair_list'),
	path('Repair/New', views.repairCreateView.as_view(), name='repair_new'),
	path('Repair/Details/<int:pk>', views.repairDetailView.as_view(), name='repair_details'),
	path('Repair/Update/<int:pk>', views.repairUpdateView.as_view(), name='repair_update'),
	path('Repair/Delete/<int:pk>', views.repairDeleteView.as_view(), name='repair_delete')

	]