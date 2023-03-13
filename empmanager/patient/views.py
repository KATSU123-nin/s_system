from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Patient

from patient.Modules.views.add_excel_data import AddExcelDataView


class PatientInfoListView(ListView):
    model = Patient
    template_name = 'patient/patientinfo_list.html'
    context_object_name = 'patient_info_list'


class AddExcelData(AddExcelDataView):
    pass
