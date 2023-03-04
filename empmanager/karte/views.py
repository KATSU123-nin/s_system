from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import KarteInfo

from django.forms import Textarea
from django.forms import CheckboxSelectMultiple



class KarteInfoListView(ListView):
    model = KarteInfo
    template_name = 'index.html'
    context_object_name = 'karte_info_list'
    

class KarteInfoCreateView(CreateView):
    model = KarteInfo
    fields = ['patient', 'reha_at', 'pain', 'range', 'rehaplan', 'comment']
    template_name = 'karte/karteinfo_form.html'
    widgets = {
        'comment': Textarea(attrs={'rows': 7}),
        'rehaplan': CheckboxSelectMultiple,
    }