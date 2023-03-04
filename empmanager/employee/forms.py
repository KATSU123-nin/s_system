from django import forms
from .models import Therapist, Insurance

class SearchForm(forms.Form):
  therapist = forms.ModelChoiceField(
    queryset=Therapist.objects, label='セラピスト名', required=False
  )

  insurance = forms.ModelChoiceField(
    queryset=Insurance.objects, label='保険名', required=False
  )
