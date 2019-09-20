from django.urls import path
from . import views


urlpatterns = [
	path('repairs/', views.Repair, name='Car_repair'),
	path('repair_list/', views.Repair_list, name='Repair_list'),

]