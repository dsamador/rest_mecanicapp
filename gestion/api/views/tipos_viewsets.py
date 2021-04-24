from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from gestion.api.serializers.tipos_serializers import TipoLavadoSerializer


class TipoLavadoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoLavadoSerializer

    def get_queryset(self, pk = None):
        
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tipo de lavado creado correctamente!'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)