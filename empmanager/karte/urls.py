from django.urls import path
from . import views


app_name = 'karte'

urlpatterns = [
    path('',views.KarteInfoListView.as_view(), name='index'),
    path('create/', views.KarteInfoCreateView.as_view(), name='karteinfo_create'),
]

