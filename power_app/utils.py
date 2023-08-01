from datetime import timedelta
from django.utils import timezone
from .models import Asistencia, Usuario

def delete_old_asistencias():
    # Calculate the date 4 months ago from the current date
    four_months_ago = timezone.now() - timedelta(days=120)

    # Use the QuerySet filter to get Asistencia objects older than 4 months
    old_asistencias = Asistencia.objects.filter(dia__lt=four_months_ago)

    # Delete the old Asistencia objects
    old_asistencias.delete()

def delete_old_users():
    # Calculate the date 4 months ago from the current date
    six_months_ago = timezone.now() - timedelta(days=180)

    # Use the QuerySet filter to get Asistencia objects older than 4 months
    old_users = Usuario.objects.filter(vencimiento__lt=six_months_ago)

    # Delete the old Asistencia objects
    old_users.delete()