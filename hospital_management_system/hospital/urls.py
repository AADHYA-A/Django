from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('patients/', views.patients, name='patients'),
    path('appointments/', views.appointments, name='appointments'),
    path('doctors/register_doctor/', views.register_doctor, name='register_doctor'),
    path('departments/register_department/', views.register_department, name='register_department'),
    path('patients/register_patient/', views.register_patient, name='register_patient'),
    path('appointments/book_appointment/', views.book_appointment, name='book_appointment'),
]