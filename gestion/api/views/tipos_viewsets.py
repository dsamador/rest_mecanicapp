from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from gestion.api.serializers.tipos_serializers import TipoLavadoSerializer, TipoMantenimientoSerializer, TipoCombustibleSerializer 


class TipoLavadoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoLavadoSerializer

    def get_queryset(self, pk = None):        
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request):
        tipolavado_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(tipolavado_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tipo de lavado creado correctamente!'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class TipoMantenimientoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoMantenimientoSerializer

    def get_queryset(self, pk = None):        
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request):
        tipomantenimiento_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(tipomantenimiento_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tipo de mantenimiento creado correctamente!'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class TipoCombustibleViewSet(viewsets.ModelViewSet):
    serializer_class = TipoCombustibleSerializer

    def get_queryset(self, pk = None):        
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request):
        tipocombustible_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(tipocombustible_serializer.data, status = status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tipo de combustible creado correctamente!'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
   