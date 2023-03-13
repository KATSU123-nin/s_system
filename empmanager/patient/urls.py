from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('', views.PatientInfoListView.as_view(), name='patientinfo_list'),
    path('add_excel_data/', views.AddExcelData .as_view(), name='add_excel_data'),
]
