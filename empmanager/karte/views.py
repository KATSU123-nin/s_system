from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import KarteInfo
from .forms import KarteInfoForm


class KarteInfoListView(ListView):
    model = KarteInfo
    template_name = 'index.html'
    context_object_name = 'karte_info_list'


class KarteInfoCreateView(CreateView):
    model = KarteInfo
    form_class = KarteInfoForm
    template_name = 'karteinfo_form.html'
    success_url = '/'
