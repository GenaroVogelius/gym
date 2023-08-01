from datetime import timedelta
from django.utils import timezone
from .models import Asistencia

def delete_old_asistencias():
    # Calculate the date 4 months ago from the current date
    four_months_ago = timezone.now() - timedelta(days=2)

    # Use the QuerySet filter to get Asistencia objects older than 4 months
    old_asistencias = Asistencia.objects.filter(dia__lt=four_months_ago)

    # Delete the old Asistencia objects
    old_asistencias.delete()