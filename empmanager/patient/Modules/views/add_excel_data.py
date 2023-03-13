from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from patient.models import Patient

class AddExcelDataView(TemplateView):
  template_name = 'patient/add_excel_data.html'

  def get(self, request, *args, **kwargs):
    from patient.Modules.common.get_excel_data import get_excel_data
    get_excel_data()
    return redirect(reverse_lazy('patient:patientinfo_list'))
