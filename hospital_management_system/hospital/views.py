from django.shortcuts import render, redirect
from .forms import DepartmentForm, DoctorForm, PatientForm, AppointmentForm
from .models import Department, Doctor, Patient, Appointment

def index(request):
    return render(request, 'index.html')

def departments(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments')
    else:
        form = DepartmentForm()
    return render(request, 'departments.html', {'departments': departments, 'form': form})

def doctors(request):
    doctors = Doctor.objects.all()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()
    return render(request, 'doctors.html', {'doctors': doctors, 'form': form})

def patients(request):
    patients = Patient.objects.all()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm()
    return render(request, 'patients.html', {'patients': patients, 'form': form})

def appointments(request):
    appointments = Appointment.objects.all()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointments.html', {'appointments': appointments, 'form': form})

def register_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()
    return render(request, 'register_doctor.html', {'form': form})

def register_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments')
    else:
        form = DepartmentForm()
    return render(request, 'register_department.html', {'form': form})

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm()
    return render(request, 'register_patient.html', {'form': form})

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'appointments.html', {'message': 'Appointment booked successfully'})
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})
