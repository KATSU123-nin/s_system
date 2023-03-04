from django.views import generic
from .forms import SearchForm
from .models import Employee

# Create your views here.


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

      print("Queryset", queryset)

      return queryset
