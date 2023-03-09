from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.PatientInfoListView.as_view(), name='patientinfo_list'),
]

