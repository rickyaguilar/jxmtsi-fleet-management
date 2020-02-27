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
	# FILTER BY MONTH
	path('Registration/January', views.janRegView, name='Monitoring_jan_reg'),
	path('Registration/Febuary', views.febRegView, name='Monitoring_feb_reg'),
	path('Registration/March', views.marRegView, name='Monitoring_mar_reg'),
	path('Registration/April', views.aprRegView, name='Monitoring_apr_reg'),
	path('Registration/May', views.mayRegView, name='Monitoring_may_reg'),
	path('Registration/June', views.junRegView, name='Monitoring_jun_reg'),
	path('Registration/July', views.julRegView, name='Monitoring_jul_reg'),
	path('Registration/August', views.augRegView, name='Monitoring_aug_reg'),
	path('Registration/September', views.sepRegView, name='Monitoring_sep_reg'),
	path('Registration/October', views.octRegView, name='Monitoring_oct_reg'),
	# FILTER WITHOUT TEMPLATE
	path('Plate-monitoring/', views.plateMonitoringView, name='Monitoring_plate'),
	path('Monitoring/Export', views.fata_excel, name='fata_export'),
	path('Registration/Update/<int:pk>', views.regUpdate.as_view(), name='reg_update'),
]