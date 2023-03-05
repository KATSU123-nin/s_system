from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from employee.models import Therapist
from .models import KarteInfo
from .forms import KarteInfoForm, KarteInfoSearchForm, AddPatientForm, KarteDetailInfoSearchForm
from employee.models import Employee

from django.views.generic import DetailView


class KarteInfoListView(ListView):
    model = KarteInfo
    template_name = 'karte/kateinfo_list.html'
    context_object_name = 'karte_info_list'
    paginate_by = 30
    form_class = KarteInfoSearchForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for karteinfo in context['karte_info_list']:
            # KarteInfoに関連しているEmployeeの情報はドットで繋げることで取得できる！
            # print(karteinfo.patient.therapist)
            karteinfo.therapist = karteinfo.patient.therapist

        # フォーム情報を追加
        context['form'] = KarteInfoSearchForm(self.request.GET)

        # セラピストの一覧を取得
        context['therapist_all_list'] = Therapist.objects.all()

        return context

    def get_queryset(self):
        form = KarteInfoSearchForm(self.request.GET)
        form.is_valid()

        queryset = super().get_queryset()


        patient = form.cleaned_data['patient']
        if patient:
            queryset = queryset.filter(patient=patient)

        therapist = form.cleaned_data['therapist']
        if therapist:
            queryset = queryset.filter(patient__therapist=therapist)

        return queryset


# カルテ情報を追加する
class KarteInfoCreateView(CreateView):
    model = KarteInfo
    form_class = KarteInfoForm
    template_name = 'karte/karteinfo_form.html'
    success_url = reverse_lazy('karte:karteinfo_list')

class AddPatientCreateView(CreateView):
    model = Employee
    form_class = AddPatientForm
    template_name = 'karte/addpatient_form.html'
    success_url = reverse_lazy('karte:karteinfo_list')


class TherapistKarteListDetailView(DetailView):
    model = Therapist
    template_name = 'karte/therapistkartelist_detail.html'
    context_object_name = 'karte_detail_info_list'
    form_class = KarteDetailInfoSearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        therapist = self.get_object()
        context['karte_detail_info_list'] = KarteInfo.objects.filter(patient__therapist=therapist)

        context['therapist_all_list'] = Therapist.objects.all()

        return context


class KarteInfoDetailView(DetailView):
    model = KarteInfo
    template_name = 'karte/karteinfo_detail.html'


class IdPatientKarteDetailView(DetailView):
    model = KarteInfo
    template_name = 'karte/id_patient_karte_detail.html'
    context_object_name = 'id_patient_karte_detail'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_id = self.kwargs['pk']
        context['id_karteinfo_list'] = KarteInfo.objects.filter(patient=patient_id)
        return context

