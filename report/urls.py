from django.urls import path
from . import views

urlpatterns = [
	path('Report/', views.reportListView.as_view(), name= 'report_list'),
	path('Report/New', views.report_new, name='report_new'),
	path('Report/Submit', views.report_submit, name='report_submit'),
	path('Report/Export', views.report_excel, name='report_export'),
	path('Report/Update/<int:pk>', views.reportUpdate.as_view(), name='report_update'),
	path('Report/Details/<int:pk>', views.reportDetails.as_view(), name='report_details'),
	path('Report/Delete/<int:pk>', views.reportDeleteView.as_view(), name='report_delete'),
	path('Report/History/', views.reportHistoryView, name='report_history'),

]