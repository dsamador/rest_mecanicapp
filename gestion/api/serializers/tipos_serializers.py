from gestion.models import TipoLavado, TipoMantenimiento, TipoCombustible, TipoVehiculo
from rest_framework import serializers

class TipoLavadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLavado
        exclude = ('state','created_date','modified_date','deleted_date')
    
    def to_representation(self, instance):
        return {
            'nombre': instance.nombre,
            'descripcion': instance.descripcion
        }