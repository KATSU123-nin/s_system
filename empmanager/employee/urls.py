from django.urls import path
from . import views


app_name = 'employee'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('detail/patient/<int:pk>', views.IdPatientInfoDetailView.as_view(), name="idpatientinfo_detail")
]

