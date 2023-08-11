from datetime import timedelta
from django.utils import timezone
from .models import Asistencia, Usuario

def delete_old_asistencias():
    # Calculate the date 13 months ago from the current date
    thirteen_months_ago = timezone.now() - timedelta(days=390)

    # Use the QuerySet filter to get Asistencia objects older than 13 months
    old_asistencias = Asistencia.objects.filter(dia__lt=thirteen_months_ago)

    # Delete the old Asistencia objects
    old_asistencias.delete()

def delete_old_users():
    # Calculate the date 13 months ago from the current date
    thirteen_months_ago = timezone.now() - timedelta(days=390)

    # Use the QuerySet filter to get Asistencia objects older than 13 months
    old_users = Usuario.objects.filter(vencimiento__lt=thirteen_months_ago)

    # Delete the old Asistencia objects
    old_users.delete()