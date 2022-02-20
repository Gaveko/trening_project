from django.urls import path

from . import views

urlpatterns = [
    path('doctor/', views.DoctorListView.as_view()),
    path('patient/', views.PatientViewSet.as_view({'get': 'list', 'post': 'create'})),
]