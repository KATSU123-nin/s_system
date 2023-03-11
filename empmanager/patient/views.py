from django.views.generic import ListView
from .models import Patient

class PatientInfoListView(ListView):
  model = Patient
  template_name = 'patient/patientinfo_list.html'
  context_object_name = 'patient_info_list'


