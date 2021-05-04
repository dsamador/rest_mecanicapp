from rest_framework import serializers
from gestion.models import MarcaVehiculo

class MarcaVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarcaVehiculo
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre            
        }