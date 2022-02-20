from django.contrib import admin

from .models import RecordToDoctor, Patient, Doctor, DoctorDay, DoctorTimeStamp, MedicalService

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicalService)
admin.site.register(RecordToDoctor)
admin.site.register(DoctorDay)
admin.site.register(DoctorTimeStamp)

