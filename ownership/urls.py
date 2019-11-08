from django.urls import path
from . import views

urlpatterns = [
    path('Ownership/', views.ownershipListView.as_view(), name= 'ownership_list'),
    path('Ownership/New', views.ownershipCreateView.as_view(), name='ownership_new'),
    path('Ownership/Update/<int:pk>', views.ownershipUpdate.as_view(), name='ownership_update'),
    path('Ownership/Details/<int:pk>', views.ownershipDetails.as_view(), name='ownership_details'),
    path('Ownership/Delete/<int:pk>', views.ownershipDeleteView.as_view(), name='ownership_delete'),

    ]