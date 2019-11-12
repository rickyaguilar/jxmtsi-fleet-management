from django.urls import path
from . import views

urlpatterns = [
	path('Voucher/', views.voucherListView.as_view(), name= 'voucher_list'),
	path('Voucher/new', views.voucherCreateView.as_view(), name='voucher_new'),
	path('Voucher/Update/<int:pk>', views.voucherUpdate.as_view(), name='voucher_update'),
	path('Voucher/Details/<int:pk>', views.voucherDetails.as_view(), name='voucher_details'),
	path('Voucher/Delete/<int:pk>', views.voucherDeleteView.as_view(), name='voucher_delete'),
]