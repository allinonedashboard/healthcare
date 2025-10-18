from django.contrib import admin
from .models import Profile, Doctor, Patient, Hospital, Appointment, MedicalRecord
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
