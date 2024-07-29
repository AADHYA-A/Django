from django import forms
from .models import Department, Doctor, Patient, Appointment

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'department']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'doctor', 'admission_date', 'disease']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date', 'description']