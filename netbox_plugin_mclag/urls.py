from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (

    # McDomain
    path('domains/', views.McDomainListView.as_view(), name='mcdomain_list'),
    path('domains/add/', views.McDomainEditView.as_view(), name='mcdomain_add'),
    path('domains/<int:pk>/', views.McDomainView.as_view(), name='mcdomain'),
    path('domains/<int:pk>/edit/', views.McDomainEditView.as_view(), name='mcdomain_edit'),
    path('domains/<int:pk>/delete/', views.McDomainDeleteView.as_view(), name='mcdomain_delete'),
    path('domains/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='mcdomain_changelog', kwargs={
        'model': models.McDomain
    }),

    # McLag
    path('mclags/', views.McLagListView.as_view(), name='mclag_list'),
    path('mclags/add/', views.McLagEditView.as_view(), name='mclag_add'),
    path('mclags/<int:pk>/', views.McLagView.as_view(), name='mclag'),
    path('mclags/<int:pk>/edit/', views.McLagEditView.as_view(), name='mclag_edit'),
    path('mclags/<int:pk>/delete/', views.McLagDeleteView.as_view(), name='mclag_delete'),
    path('mclags/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='mclag_changelog', kwargs={
        'model': models.McLag
    }),

)