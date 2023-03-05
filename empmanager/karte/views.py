from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from employee.models import Therapist
from .models import KarteInfo
from .forms import KarteInfoForm, KarteInfoSearchForm

from django.views.generic import DetailView


class KarteInfoListView(ListView):
    model = KarteInfo
    template_name = 'karte/index.html'
    context_object_name = 'karte_info_list'
    paginate_by = 10
    form_class = KarteInfoSearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for karteinfo in context['karte_info_list']:
            # KarteInfoに関連しているEmployeeの情報はドットで繋げることで取得できる！
            # print(karteinfo.patient.therapist)
            karteinfo.therapist = karteinfo.patient.therapist

        # フォーム情報を追加
        context['form'] = KarteInfoSearchForm(self.request.GET)

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



class TherapistDetailView(DetailView):
    model = Therapist
    template_name = 'karte/therapist_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        therapist = self.object
        context['karteinfo_list'] = KarteInfo.objects.filter(therapist=therapist)
        return context


class KarteInfoDetailView(DetailView):
    model = KarteInfo
    template_name = 'karte/karteinfo_detail.html'
