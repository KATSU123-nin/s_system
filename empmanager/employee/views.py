from django.views import generic
from .forms import SearchForm, KarteDetailInfoSearchForm
from .models import Employee
from karte.models import KarteInfo


class IndexView(generic.ListView):
    model = Employee

    def get_context_data(self):
        context = super().get_context_data()
        context["form"] = SearchForm(self.request.GET)

        print("Context", context)

        return context

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        form.is_valid()

        queryset = super().get_queryset()

        insurance = form.cleaned_data['insurance']
        if insurance:
            queryset = queryset.filter(insurance=insurance)

        therapist = form.cleaned_data['therapist']
        if therapist:
            queryset = queryset.filter(therapist=therapist)

        # print("Queryset", queryset)
        return queryset


class IdPatientInfoDetailView(generic.DetailView):
    model = Employee
    template_name = 'employee/id_patient_info_detail.html'
    context_object_name = 'id_patient_info'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_id = self.kwargs['pk']
        context['id_karteinfo_list'] = KarteInfo.objects.filter(
            patient=patient_id)
        context['id_employeeinfo_list'] = Employee.objects.filter(
            id=patient_id)
        context['form'] = KarteDetailInfoSearchForm()
        return context

    def get_queryset(self):
        form = KarteDetailInfoSearchForm(self.request.GET)
        form.is_valid()

        queryset = super().get_queryset()

        patient_name = form.cleaned_data['patient_name']
        if patient_name:
            queryset = queryset.filter(patient=patient_name)
            print("TTTTTTTTTTTTTTT", patient_name)

        print("Q QQQQQQQQQQQQQQQueryset", queryset)
        return queryset
