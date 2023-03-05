from django.urls import path
from . import views

app_name = 'karte'

urlpatterns = [
    path('',views.KarteInfoListView.as_view(), name='karteinfo_list'),
    path('create/', views.KarteInfoCreateView.as_view(), name = 'karteinfo_create'),
    path('therapist/<int:pk>/', views.TherapistDetailView.as_view(), name='therapist_detail'),
    path('karteinfo/<int:pk>/', views.KarteInfoDetailView.as_view(), name='karteinfo_detail'),
]

