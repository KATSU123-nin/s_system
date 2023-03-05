from django import forms
from .models import KarteInfo

class KarteInfoForm(forms.ModelForm):
    class Meta:
        model = KarteInfo
        fields = ('patient', 'reha_at', 'pain', 'range', 'rehaplan', 'comment')
        widgets = {
            'rehaplan': forms.CheckboxSelectMultiple(),
        }
