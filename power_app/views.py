

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *



@api_view(['GET', 'POST'])
def usuario(request, dni):
    if request.method == 'GET':
        try:
            usuario = Usuario.objects.get(DNI = dni)
            serializer = UsuarioSerializer(usuario, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'not found': f'Usuario with DNI {dni} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'POST':
        try:
            user = Usuario.objects.get(DNI=dni)
            Asistencia.objects.create(
                usuario = user
            )
            return Response({"message": "asistencia tomada"}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'not found': f'Usuario with DNI {dni} does not exist'}, status=status.HTTP_400_BAD_REQUEST)









