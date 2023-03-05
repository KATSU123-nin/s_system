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



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        print('@@@@@@@@@@@@@@@@@@@@')
        print('self.initial.get'.upper(), super().__init__(*args, **kwargs))

        # if 'therapist' in self.data:
        #     therapist_id = self.data.get('therapist')
        #     self.fields['patient'].queryset = Employee.objects.filter(therapist=therapist_id)

            # print('@@@@@@@@@@@@@@@@@@@@')
            # print('self.data.get("therapist")'.upper(), therapist_id)

        # print('@@@@@@@@@@@@@@@@@@@@')
        # print('self.data'.upper(), self.data)

        # print('@@@@@@@@@@@@@@@@@@@@')
        # print('Employee.objects.filter(Therapist=therapist_id)'.upper(),Employee.objects.filter(therapist=True))

        # print('@@@@@@@@@@@@@@@@@@@@')
        # print('self.fields'.upper(), self.fields['patient'].queryset)



class KarteInfoForm(forms.ModelForm):
    reha_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = KarteInfo
        fields = ('patient', 'reha_at', 'pain', 'range', 'rehaplan', 'comment')
        widgets = {
            'rehaplan': forms.CheckboxSelectMultiple(),
        }
