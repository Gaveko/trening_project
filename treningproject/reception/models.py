from django.contrib.auth import get_user_model
from django.db import models

from .constants import SPECIALIZATION_CHOICES

User = get_user_model()


class ClinicUser(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=15)

    class Meta:
        abstract = True


class Patient(ClinicUser):
    email = models.EmailField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'Patient {self.first_name} {self.last_name}'


class Doctor(ClinicUser):
    specialization = models.IntegerField(choices=SPECIALIZATION_CHOICES)
    start_work_time = models.TimeField()
    end_work_time = models.TimeField()
    admission_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Doctor {self.first_name} {self.last_name} - {self.specialization}'


class MedicalService(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class RecordToDoctor(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medical_services = models.ManyToManyField(MedicalService, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Record of {self.patient} to {self.doctor}'


class DoctorDay(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class DoctorTimeStamp(models.Model):
    doctor_day = models.ForeignKey(DoctorDay, on_delete=models.CASCADE)
    start_time_stamp = models.TimeField()
    end_time_stamp = models.TimeField()
    is_busy = models.BooleanField(default=False)


