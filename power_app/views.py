# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *
from django.contrib import messages
import pandas
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime, time
import json
from django.db.models import Q


@api_view(["GET", "POST"])
def usuario(request, dni):
    if request.method == "GET":
        try:
            usuario = Usuario.objects.get(DNI=dni)
            serializer = UsuarioSerializer(usuario, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response(
                {"not found": f"Usuario with DNI {dni} does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    if request.method == "POST":
        try:
            user = Usuario.objects.get(DNI=dni)
            Asistencia.objects.create(usuario=user)
            return Response({"message": "asistencia tomada"}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response(
                {"not found": f"Usuario with DNI {dni} does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

def upload_excel(self, request):
        if request.method == "POST":
            excel_file = request.FILES["excel_upload"]
        
            if not excel_file.name.endswith('.xlsx'):
                messages.warning(request, 'The wrong file type was uploaded')
                url = reverse('admin:index')
                return HttpResponseRedirect(url)
        
            # Load the Excel file into a Pandas DataFrame
            data_frame = pandas.read_excel(excel_file)
            
            # Iterate over the rows of the DataFrame and create or update instances of the Usuario model
            for index, row in data_frame.iterrows():
                Usuario.objects.update_or_create(
                    nombre=row['nombre'],
                    apellido=row['apellido'],
                    sexo=row['sexo'],
                    DNI=row['DNI'],
                    pago=row['pago'],
                    vencimiento= row['vencimiento'],
                )
                
            return HttpResponseRedirect(reverse('admin:index'))

def graphics(request):
    time_ranges = [
    time(8, 0), time(8, 30), time(9, 0), time(9, 30), time(10, 0),
    time(10, 30), time(11, 0), time(11, 30), time(12, 0),
    time(12, 30), time(13, 0), time(13, 30), time(14, 0),
    time(14, 30), time(15, 0), time(15, 30), time(16, 0),
    time(16, 30), time(17, 0), time(17, 30), time(18, 0),
    time(18, 30), time(19, 0), time(19, 30), time(20, 0),
    time(20, 30), time(21, 0)
]
    # ? enves de escribir time_ranges con lo que esta en slices es lo mismo
    SLICES = [time(hour, minute) for hour in range(7, 22) for minute in (0, 30)]
    
    
    # Calculate the date range for the past 7 days
    seven_days_ago = timezone.now() - timedelta(days=7)

    # Query for Asistencia objects with 'dia' not more than 7 days ago
    asistencias = Asistencia.objects.filter(dia__range=(seven_days_ago, timezone.now()))
    # Now 'asistencias' contains instances with 'dia' not more than 7 days ago

    # creas un dataframe con los objetos
    asistencias_df = pandas.DataFrame(asistencias.values())



    def categorize_time(time_row):
        for first, second in zip(SLICES[::1], SLICES[1::1]):
            if first <= time_row < second:
                return str(first)[:-3]
        return None
    # !tambien podes iterar para comparar entre 2 asi:
    # def categorize_time(time_row):
    #   for i in range(len(slices) - 1):
    #     if slices[i] <= time_row < slices[i+1]:
    #         return str(slices[i])[:-3]
    # return None


    # Apply the function categorize_time to 'hora' column and create a new column
    asistencias_df['time_slice'] = asistencias_df['hora'].apply(categorize_time)

    

    # groups your DataFrame by the unique values in the 'dia' and 'time_slice' column, haciendo que cada dia tenga su time_slice y por cada time_slice cuenta cuantos hay y crea una columna llamada persons_arrive_per_time que contiene ese valor.
    time_slice_counts_per_day_df = asistencias_df.groupby(['dia', 'time_slice']).size().reset_index(name='persons_arrive_per_time')
    

    def change_date_order(date):
        year, month, day = str(date).split('-')
        return f'{day}-{month}'

    #? es para cambiar el formato de año-mes-dia a dia/mes
    time_slice_counts_per_day_df['dia'] = time_slice_counts_per_day_df['dia'].apply(change_date_order)


    daily_total_arrivals = time_slice_counts_per_day_df.groupby('dia')['persons_arrive_per_time'].sum()
    json_data_pandas_daily_total_arrivals = daily_total_arrivals.to_json(orient='index')
    # Load JSON data into a Python dictionary
    daily_total_arrivals_dict = json.loads(json_data_pandas_daily_total_arrivals)


    def dict_time_count(row):
        return {time: count for time, count in zip(row['time_slice'], row['persons_arrive_per_time'])}

    # Group by 'dia' and apply the function to each group, reset_index es para que la columna que tiene los diccionarios se llame time_counts
    day_and_time_df = time_slice_counts_per_day_df.groupby('dia').apply(dict_time_count).reset_index(name='time_counts')

    

    # ?inplace es True: El DataFrame original se modificará directamente y no se devolverá un nuevo DataFrame
    day_and_time_df.set_index('dia', inplace=True)


    

    # ?con orient index vas a utilizar el indice como key el resto como value
    json_data_pandas = day_and_time_df.to_json(orient='index')

    # Load JSON data into a Python dictionary
    days_and_times_dict = json.loads(json_data_pandas)

    days_list = list(days_and_times_dict.keys())

    print(days_list)
    print(days_and_times_dict)

    four_months_ago = timezone.now() - timedelta(days=30 * 4)

    # Query for Usuario objects with vencimiento not less than 4 months ago
    users =  Usuario.objects.filter(Q(vencimiento__gte=four_months_ago) | Q(vencimiento__isnull=True))
    users_df = pandas.DataFrame(list(users.values()))

    sexo_counts_dict = (
        users_df["sexo"].value_counts().to_dict()
    )
    
    print(daily_total_arrivals_dict)

        
    return render(
        request,
        "graphics.html", {"llegadas_data":1, "horarios_dict" : days_and_times_dict, "days_list":days_list, }
    )


