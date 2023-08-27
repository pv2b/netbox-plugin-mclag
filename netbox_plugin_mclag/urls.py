from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (

    # McDomain
    path('domains/', views.McDomainListView.as_view(), name='mc_domain_list'),
    path('domains/add/', views.McDomainEditView.as_view(), name='mc_domain_add'),
    path('domains/<int:pk>/', views.McDomainView.as_view(), name='mc_domain'),
    path('domains/<int:pk>/edit/', views.McDomainEditView.as_view(), name='mc_domain_edit'),
    path('domains/<int:pk>/delete/', views.McDomainDeleteView.as_view(), name='mc_domain_delete'),
    path('domains/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='mc_domain_changelog', kwargs={
        'model': models.McDomain
    }),

    # McLag
    path('mclags/', views.McLagListView.as_view(), name='mc_lag_list'),
    path('mclags/add/', views.McLagEditView.as_view(), name='mc_lag_add'),
    path('mclags/<int:pk>/', views.McLagView.as_view(), name='mc_lag'),
    path('mclags/<int:pk>/edit/', views.McLagEditView.as_view(), name='mc_lag_edit'),
    path('mclags/<int:pk>/delete/', views.McLagDeleteView.as_view(), name='mc_lag_delete'),
    path('mclags/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='mc_lag_changelog', kwargs={
        'model': models.McLag
    }),

)