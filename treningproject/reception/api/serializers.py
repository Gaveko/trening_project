from rest_framework.serializers import ModelSerializer

from ..models import Doctor, Patient


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'