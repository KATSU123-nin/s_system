from django import forms
from .models import KarteInfo

from django import forms
from .models import Employee,KarteInfo
from employee.models import Therapist


class KarteInfoSearchForm(forms.Form):
    therapist = forms.ModelChoiceField(
        queryset=Therapist.objects.all(), label='担当セラピスト', required=False)

    patient = forms.ModelChoiceField(
        queryset=Employee.objects.all(), label='患者名', required=False)


class KarteInfoForm(forms.ModelForm):
    reha_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = KarteInfo
        fields = ('patient', 'reha_at', 'pain', 'range', 'rehaplan', 'comment')
        widgets = {
            'rehaplan': forms.CheckboxSelectMultiple(),
        }
