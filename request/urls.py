from django.urls import path
from . import views
from .views import (
  	requestCreateView,
  	requestListView,
	requestDetailView,
	requestUpdateView,
	requestDeleteView,
 )

urlpatterns = [
	path('Request/', requestListView.as_view(), name='carrequest_list'),
	path('Request/New', requestCreateView.as_view(), name='car_request'),
	path('Request/Details/<int:pk>/', requestDetailView.as_view(), name='carrequest_details'),
	path('Request/Update/<int:pk>/', requestUpdateView.as_view(), name='carrequest_update'),
	path('Request/Delete/<int:pk>/', requestDeleteView.as_view(), name='carrequest_delete'),

]