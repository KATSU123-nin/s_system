from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import KarteInfo
from .forms import KarteInfoForm
from .forms import KarteInfoSearchForm


class KarteInfoListView(ListView):
    model = KarteInfo
    template_name = 'karte/index.html'
    context_object_name = 'karte_info_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        print("context['karte_info_list']".upper(), context['karte_info_list'])
        """
        セラピスト情報を追加

        context内のkarte_info_listには以下のQuerySet（データベース内のデータ）が含まれている。
        CONTEXT['KARTE_INFO_LIST'] <QuerySet [<KarteInfo: 山田 太郎>, <KarteInfo: 高橋 四郎>, <KarteInfo: 太田 五郎>, <KarteInfo: 高橋 四郎>, <KarteInfo: 高橋 四郎>, <KarteInfo: 高橋 四郎>, <KarteInfo: 太田 五郎>]>

        そのため、１つ１つのKarteInfoを取り出して、thrapistの情報を追加している。
        """
        for karteinfo in context['karte_info_list']:
          # KarteInfoに関連しているEmployeeの情報はドットで繋げることで取得できる！
          print(karteinfo.patient.therapist)
          karteinfo.therapist = karteinfo.patient.therapist

        # フォーム情報を追加
        context['form'] = KarteInfoSearchForm(self.request.GET)
        print("CONTEXT:KARTE",context)
        return context

    def get_queryset(self):
      form = KarteInfoSearchForm(self.request.GET)
      form.is_valid()

      queryset = super().get_queryset()
      patient = form.cleaned_data['patient']
      # print("PPP",form.cleaned_data)

      if patient:
        queryset = queryset.filter(patient=patient)

      # print("GETGETFORM",self.request.GET)
      # print("QUERYSET:KARTE",super().get_queryset())
      return queryset

# カルテ情報を追加する
class KarteInfoCreateView(CreateView):
    model = KarteInfo
    form_class = KarteInfoForm
    template_name = 'karte/karteinfo_form.html'
    success_url = reverse_lazy('karte:karteinfo_list')
