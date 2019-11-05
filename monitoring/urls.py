from django.urls import path
from . import views

urlpatterns = [
	path('Monitoring/', views.monitoringListView.as_view(), name= 'Monitoring_list'),
	path('Monitoring/new', views.monitoringCreateView.as_view(), name='Monitoring_new'),
	path('Monitoring/Update/<int:pk>', views.monitoringUpdate.as_view(), name='Monitoring_update'),
	path('Monitoring/Details/<int:pk>', views.monitoringDetails.as_view(), name='Monitoring_details'),
	path('Monitoring/Delete/<int:pk>', views.monitoringDeleteView.as_view(), name='Monitoring_delete'),
]