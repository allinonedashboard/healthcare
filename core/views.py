from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, AppointmentForm, MedicalRecordForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Patient, Doctor, Appointment, MedicalRecord
from django.contrib.auth.models import User
from django.utils import timezone

def home(request):
    return render(request, "home.html")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
                first_name=data["first_name"],
                last_name=data["last_name"],
            )
            role = request.POST.get("role", "patient")
            profile = Profile.objects.create(user=user, role=role)
            if role == "patient":
                Patient.objects.create(profile=profile)
            else:
                Doctor.objects.create(profile=profile, specialization="General")
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("dashboard")
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)
    # get patient or doctor objects if exist
    patient = getattr(profile, "patient", None)
    doctor = getattr(profile, "doctor", None)
    appointments = []
    records = []
    if patient:
        appointments = Appointment.objects.filter(patient=patient).order_by("date", "time")
        records = MedicalRecord.objects.filter(patient=patient).order_by("-uploaded_at")
    elif doctor:
        appointments = Appointment.objects.filter(doctor=doctor).order_by("date", "time")
    return render(request, "dashboard.html", {"profile": profile, "appointments": appointments, "records": records})

@login_required
def book_appointment(request):
    profile = Profile.objects.get(user=request.user)
    if not hasattr(profile, "patient"):
        return redirect("dashboard")
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            appt.patient = profile.patient
            appt.save()
            return redirect("dashboard")
    else:
        form = AppointmentForm()
        # restrict doctors in form to existing doctor objects
        form.fields["doctor"].queryset = Doctor.objects.all()
    return render(request, "book_appointment.html", {"form": form})

@login_required
def upload_record(request):
    profile = Profile.objects.get(user=request.user)
    if not hasattr(profile, "patient"):
        return redirect("dashboard")
    if request.method == "POST":
        form = MedicalRecordForm(request.POST, request.FILES)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.patient = profile.patient
            rec.save()
            return redirect("dashboard")
    else:
        form = MedicalRecordForm()
    return render(request, "upload_record.html", {"form": form})
