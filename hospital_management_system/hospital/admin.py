from django.contrib import admin
from .models import Department, Doctor, Patient, Appointment

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'specialization')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor', 'admission_date', 'disease')
    list_filter = ('doctor', 'admission_date')
    search_fields = ('name', 'doctor__name', 'disease')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'description')
    list_filter = ('doctor', 'appointment_date')
    search_fields = ('patient__name', 'doctor__name', 'description')