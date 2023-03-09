from django import forms
from .models import Therapist, Insurance, Employee

class SearchForm(forms.Form):
  therapist = forms.ModelChoiceField(
    queryset=Therapist.objects, label='セラピスト名', required=False
  )

  insurance = forms.ModelChoiceField(
    queryset=Insurance.objects, label='保険名', required=False
  )

class KarteDetailInfoSearchForm(forms.Form):
    patient_name = forms.CharField(max_length=255, required=False)
    patient = forms.ModelChoiceField(
        queryset=Employee.objects.all(), label='患者名', required=False)
