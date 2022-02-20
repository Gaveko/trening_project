from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from .serializers import DoctorSerializer, PatientSerializer
from ..models import Doctor, Patient, DoctorDay


class DoctorListView(ListAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class PatientViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class RecordToDoctor(APIView):
    def get(self, request, *args, **kwargs):
        doctor_id = kwargs['doctor_id']
        doctor = Doctor.objects.get(pk=doctor_id)


    def post(self, request, *args, **kwargs):
        pass
