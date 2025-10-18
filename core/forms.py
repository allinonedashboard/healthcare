from django import forms
from django.contrib.auth.models import User
from .models import MedicalRecord, Appointment

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=(("patient","Patient"),("doctor","Doctor")))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "date", "time", "notes"]

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ["title", "file"]
