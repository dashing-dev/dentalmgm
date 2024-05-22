
from django.contrib import admin 
from django.urls import path , include 
from . import views 

urlpatterns = [
    path("", views.index , name='index'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('view_patient/', views.view_patient, name='view_patient'),
    path('patient_list/', views.patient_list ,name='patient_list'),
    path('patient/<int:pk>/', views.patient_view, name='patient'),
    path('patients/', views.patients_view, name='patients'),
    path('patient/<int:pk>/', views.patient_view, name='patient'),
    path('patient-redirect/<int:pk>/', views.patient_redirect_view, name='patient-redirect'),
    path('searchpatients', views.search_patients, name='search_patients'),

]
