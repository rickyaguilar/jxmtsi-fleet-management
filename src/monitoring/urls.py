from django.urls import path
from . import views

urlpatterns = [
	path('Monitoring/', views.monitoringListView.as_view(), name= 'Monitoring_list'),
	path('Monitoring/New', views.monitoring_create, name='Monitoring_new'),
	path('Monitoring/Submit', views.monitoring_submit, name='Monitoring_submit'),
	path('Monitoring/Update/<int:pk>', views.monitoringUpdate.as_view(), name='Monitoring_update'),
	path('Monitoring/Details/<int:pk>', views.monitoringDetails.as_view(), name='Monitoring_details'),
	path('Monitoring/Delete/<int:pk>', views.monitoringDeleteView.as_view(), name='Monitoring_delete'),
	path('Monitoring/History/', views.monitoringHistoryView, name='Monitoring_history'),
	path('Monitoring/Export', views.fata_excel, name='fata_export'),
]