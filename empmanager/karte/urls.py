from django.urls import path
from . import views

app_name = 'karte'

urlpatterns = [
    path('',views.KarteInfoListView.as_view(), name='karteinfo_list'),
    path('create/', views.KarteInfoCreateView.as_view(), name = 'karteinfo_create'),
    path('create/patient', views.AddPatientCreateView.as_view(), name = 'addpatient_create'),
    path('detail/therapist/<int:pk>', views.TherapistKarteListDetailView.as_view(), name='therapistkartelist_detail'),
    path('detail/karteinfo/<int:pk>', views.KarteInfoDetailView.as_view(), name='karteinfo_detail'),
    path('detail/karte/<int:pk>', views.IdPatientKarteDetailView.as_view(), name="idpatientkarte_detail")
]

