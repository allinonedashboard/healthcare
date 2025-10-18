from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (
    ("patient", "Patient"),
    ("doctor", "Doctor"),
    ("admin", "Admin"),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="patient")
    phone = models.CharField(max_length=30, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Doctor(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Dr. {self.profile.user.get_full_name() or self.profile.user.username} - {self.specialization}"

class Patient(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return f"{self.profile.user.get_full_name() or self.profile.user.username}"

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default="scheduled")  # scheduled, cancelled, done
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} {self.time} - {self.patient}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="records/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.patient}"
