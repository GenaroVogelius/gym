
from rest_framework import serializers

from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ('nombre', 'activo', 'sexo', 'vencimiento',)

# exclude lleva, porque tiene que ser una tupla.
        
        
# from rest_framework import serializers importaste esto e hiciste esto sexo = serializers.StringRelatedField() para que en sexo no te muestre el id, sino enves de mostrarte masculino o femenino te muestra 1 o 2. Aparte de haber hecho esto aca, en models es importante haber usado el metodo __str__ y poner self.(nombre del field que queres que aparezca.)