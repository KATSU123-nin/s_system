from django import forms
from .models import KarteInfo

from django import forms
from .models import Employee

class KarteInfoSearchForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=Employee.objects.all(), label='患者名', required=False)

class KarteInfoForm(forms.ModelForm):
    reha_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = KarteInfo
        fields = ('patient', 'reha_at', 'pain', 'range', 'rehaplan', 'comment')
        widgets = {
            'rehaplan': forms.CheckboxSelectMultiple(),
        }
